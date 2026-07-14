import json
import os
import re

import markdown
from django.conf import settings
from django.core.cache import cache
from django.core.management.base import BaseCommand
from wagtail.models import Page, Site

from pages.models import ContactPage, ContentPage

DOMAIN_RE = re.compile(r"https?://(?:www\.)?fascinatingdentistry\.com")


def extract_schemas(text):
    """Lift each ```json ... ``` fenced block (schema.org JSON-LD).
    Handles unclosed fences (block runs to end of file)."""
    blocks = []
    for part in text.split("```json")[1:]:
        end = part.find("```")
        if end != -1:
            block = part[:end].strip()
        else:
            block = part.strip()  # no closing fence — take rest of file
        if block:
            blocks.append(block)
    return blocks


def load_md(path):
    text = open(path, encoding="utf-8").read()
    slug = re.search(r"\*\*Slug:\*\*\s*(.*)", text).group(1).strip()
    seo_title = re.search(r"\*\*Meta Title:\*\*\s*(.*)", text).group(1).strip()
    meta_desc = re.search(r"\*\*Meta Description:\*\*\s*(.*)", text).group(1).strip()
    h1_match = re.search(r"^#\s+(.+)$", text, re.M)
    h1 = h1_match.group(1).strip() if h1_match else seo_title
    body_md = text[h1_match.end():].strip() if h1_match else text
    # Strip ```json schema blocks from the body — they're extracted separately
    # for the <head> and must NOT appear as visible code blocks on the page.
    body_md = re.sub(r"```json.*?(?:```|$)", "", body_md, flags=re.DOTALL)
    html = markdown.markdown(body_md, extensions=["extra"])
    html = DOMAIN_RE.sub("", html)  # make internal links relative
    schemas = extract_schemas(text)
    # If no schema blocks in the md, generate basic WebPage + BreadcrumbList
    if not schemas:
        _su = "https://fascinatingdentistry.com"
        schemas = [
            json.dumps({"@context": "https://schema.org", "@type": "WebPage", "name": h1, "description": meta_desc, "inLanguage": "en-AU"}),
            json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{_su}/"},
                {"@type": "ListItem", "position": 2, "name": h1, "item": f"{_su}{slug}"},
            ]}),
        ]
    return slug, seo_title, meta_desc, h1, html, schemas


class Command(BaseCommand):
    help = "Create a ContentPage for each markdown file in /content (one per file)."

    def handle(self, *args, **options):
        home = Site.objects.first().root_page
        content_dir = settings.BASE_DIR / "content"
        # Only process numbered content-page files (02-13, and future 14+).
        # This excludes:
        #   01-*        (homepage, australia hub — seeded elsewhere)
        #   blog-*      (blog hub/posts — wrong model for ContentPage)
        #   *.markdown  (blog-hub.markdown — wrong extension)
        #   strategic-plan.md (internal doc, no Slug line → would crash load_md)
        files = sorted(
            f for f in os.listdir(content_dir)
            if f.endswith(".md") and re.match(r"^\d{2}-", f) and not f.startswith("01-")
        )

        for fname in files:
            slug_full, seo_title, meta_desc, h1, html, schemas = load_md(content_dir / fname)
            segments = [s for s in slug_full.strip("/").split("/") if s]
            leaf = segments[-1]

            # Walk to the right parent (supports nested slugs like /editorial-team/dr-anthony-au/)
            parent = home
            for seg in segments[:-1]:
                child = parent.get_children().filter(slug=seg).first()
                if child is None:
                    self.stdout.write(self.style.WARNING(
                        f"  parent '{seg}' not found for {fname}; placing under root"))
                    break
                parent = child.specific

            # The contact page uses ContactPage (renders the contact form);
            # all other content pages use ContentPage.
            model = ContactPage if leaf == "contact" else ContentPage

            # If a page already exists at this slug under the parent but as a
            # DIFFERENT model (e.g. an emergency-dentist page converted from
            # ContentPage to a directory.ServiceListiclePage), skip it — otherwise
            # we would create a competing ContentPage and collide on the slug.
            existing_any = Page.objects.child_of(parent).filter(slug=leaf).first()
            if existing_any is not None and existing_any.specific.__class__ is not model:
                self.stdout.write(self.style.WARNING(
                    f"  skipped  /{slug_full.strip('/')}/   ({fname}) — "
                    f"exists as {existing_any.specific.__class__.__name__}, not {model.__name__}"))
                continue

            existing = model.objects.child_of(parent).filter(slug=leaf).first()
            if existing is None:
                page = model(
                    title=h1, slug=leaf, body=html,
                    seo_title=seo_title, search_description=meta_desc,
                )
                if model is ContentPage:
                    page.schema_json = json.dumps(schemas)
                parent.add_child(instance=page)
                self.stdout.write(self.style.SUCCESS(f"created  /{slug_full.strip('/')}/   ({fname})"))
            else:
                existing.title = h1
                existing.body = html
                existing.seo_title = seo_title
                existing.search_description = meta_desc
                if model is ContentPage:
                    existing.schema_json = json.dumps(schemas)
                page = existing
                self.stdout.write(self.style.SUCCESS(f"updated  /{slug_full.strip('/')}/   ({fname})"))

            page.save_revision().publish()

        cache.delete("home_live_rel_paths")
        self.stdout.write(self.style.SUCCESS(f"Done — processed {len(files)} content pages"))
