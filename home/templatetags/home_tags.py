"""Template tags: live-link handling + body processing for designed content pages."""
import re

from django import template
from django.core.cache import cache
from django.utils.safestring import mark_safe

register = template.Library()

_CACHE_KEY = "home_live_rel_paths"


def _slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "section"


# Headings that introduce an FAQ block should not carry a numbered badge.
FAQ_HEADING_RE = re.compile(r"frequently asked|\bfaq\b|common questions|questions about", re.I)


def _live_relative_paths():
    paths = cache.get(_CACHE_KEY)
    if paths is None:
        from wagtail.models import Page, Site

        paths = set()
        for site in Site.objects.all():
            root_path = site.root_page.url_path
            for url_path in Page.objects.filter(live=True).values_list("url_path", flat=True):
                if url_path.startswith(root_path) and url_path != root_path:
                    paths.add(url_path[len(root_path):])
        cache.set(_CACHE_KEY, paths, 60)
    return paths


def _relative(href):
    path = href.split("?")[0].split("#")[0].strip("/")
    return (path + "/") if path else ""


def _is_external(href):
    return href.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def process_body(html):
    """Return {'html': safe_html, 'toc': [...]} with dead links neutralised and h2 anchors added."""
    try:
        from bs4 import BeautifulSoup
    except Exception:
        return {"html": mark_safe(html or ""), "toc": []}

    soup = BeautifulSoup(html or "", "html.parser")

    # The page title is rendered as the sole <h1> by the template, so a
    # leading <h1> in imported body content is a duplicate. Drop the first
    # one so the page never has two H1s.
    first_h1 = soup.find("h1")
    if first_h1 is not None:
        first_h1.decompose()

    live = _live_relative_paths()

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        if _is_external(href):
            continue
        if _relative(href) in live:
            existing = anchor.get("class", [])
            if isinstance(existing, str):
                existing = existing.split()
            if "fd-link" not in existing:
                anchor["class"] = existing + ["fd-link"]
        else:
            # Dead internal link — keep as span with light color, not clickable
            anchor.name = "span"
            del anchor["href"]
            anchor["class"] = "fd-link-pending"

    toc = []
    seen = set()
    for heading in soup.find_all("h2"):
        text = heading.get_text(strip=True)
        slug = _slugify(text)
        base, n = slug, 2
        while slug in seen:
            slug = f"{base}-{n}"
            n += 1
        seen.add(slug)
        heading["id"] = slug
        if FAQ_HEADING_RE.search(text):
            heading["class"] = heading.get("class", []) + ["fd-no-num"]
        toc.append({"id": slug, "text": text})

    # Mark the opening paragraph as a lead intro.
    first_p = soup.find("p")
    if first_p is not None:
        first_p["class"] = first_p.get("class", []) + ["lead"]

    return {"html": mark_safe(str(soup)), "toc": toc}


@register.simple_tag
def is_live_url(url):
    if not url or _is_external(url):
        return bool(url)
    return _relative(url) in _live_relative_paths()


@register.filter
def live_html(html):
    return process_body(html)["html"]


@register.filter
def live_links(html):
    """Style internal links in an HTML fragment based on whether the target
    page is live. Live links get class 'fd-link' (brand green). Dead internal
    links are converted to <span class="fd-link-pending"> (muted gray, not
    clickable) so the text stays readable but clearly isn't a working link yet.
    External links are left untouched."""
    try:
        from bs4 import BeautifulSoup
    except Exception:
        return mark_safe(html or "")
    soup = BeautifulSoup(html or "", "html.parser")
    live = _live_relative_paths()
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        if _is_external(href):
            continue  # leave external links as-is
        if _relative(href) in live:
            # Live internal link — add brand-green class
            existing = anchor.get("class", [])
            if "fd-link" not in existing:
                anchor["class"] = existing + ["fd-link"]
        else:
            # Dead internal link — keep as span with light color, not clickable
            anchor.name = "span"
            del anchor["href"]
            anchor["class"] = "fd-link-pending"
    return mark_safe(str(soup))


@register.filter
def tel(value):
    """Return a tel:-safe phone string (digits and leading '+' only), for
    click-to-call links on urgent-care pages."""
    return "".join(c for c in (value or "") if c.isdigit() or c == "+")


@register.filter
def domain(url):
    """Return the host of a URL without the leading 'www.' (for display)."""
    if not url:
        return ""
    from urllib.parse import urlparse

    net = urlparse(url).netloc
    return net[4:] if net.startswith("www.") else net
