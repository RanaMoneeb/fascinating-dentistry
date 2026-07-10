"""Sync seo_title + search_description on every page from its content/*.md file.

Reads each markdown source file's ``**Slug:**``, ``**Meta Title:**`` and
``**Meta Description:**`` lines, resolves the live page by walking the slug
path from the site root, and writes the two SEO fields.

Only touches ``seo_title`` and ``search_description`` — never title or body —
so it is safe to re-run and will not clobber manual content edits. Files
without all three lines (e.g. ``strategic-plan.md``) are skipped.
"""
import os
import re

from django.conf import settings
from django.core.management.base import BaseCommand
from wagtail.models import Site

SLUG_RE = re.compile(r"\*\*Slug:\*\*\s*(.*)")
TITLE_RE = re.compile(r"\*\*Meta Title:\*\*\s*(.*)")
DESC_RE = re.compile(r"\*\*Meta Description:\*\*\s*(.*)")


def _grab(regex, text):
    m = regex.search(text)
    return m.group(1).strip() if m else None


class Command(BaseCommand):
    help = (
        "Sync each page's seo_title + search_description from its content/*.md "
        "(or *.markdown) source file, matched by the **Slug:** path."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run", action="store_true", help="Report what would change without saving."
        )

    def handle(self, *args, **options):
        dry = options["dry_run"]
        content_dir = settings.BASE_DIR / "content"
        home = Site.objects.first().root_page

        files = sorted(
            f for f in os.listdir(content_dir)
            if f.endswith(".md") or f.endswith(".markdown")
        )

        updated, unchanged, missing, skipped = [], [], [], []

        for fname in files:
            text = (content_dir / fname).read_text(encoding="utf-8")
            slug_full = _grab(SLUG_RE, text)
            seo_title = _grab(TITLE_RE, text)
            meta_desc = _grab(DESC_RE, text)

            if not slug_full or not seo_title or not meta_desc:
                skipped.append((fname, "missing Slug / Meta Title / Meta Description"))
                continue

            segments = [s for s in slug_full.strip("/").split("/") if s]
            page = home.specific if not segments else None
            parent = home
            for seg in segments:
                child = parent.get_children().filter(slug=seg).first()
                if child is None:
                    break
                parent = child
            else:
                page = parent.specific  # leaf reached

            if page is None:
                missing.append((fname, slug_full))
                continue

            if page.seo_title == seo_title and page.search_description == meta_desc:
                unchanged.append((fname, slug_full))
                continue

            if not dry:
                page.seo_title = seo_title
                page.search_description = meta_desc
                page.save_revision().publish()
            updated.append((fname, slug_full, seo_title))

        for fname, slug, title in updated:
            tag = "WOULD UPD" if dry else "updated "
            self.stdout.write(self.style.SUCCESS(f"{tag} {slug:58} <- {title}"))
        for fname, slug in unchanged:
            self.stdout.write(f"{'ok      ':8}{slug:58} (already matches md)")
        for fname, slug in missing:
            self.stdout.write(self.style.ERROR(f"MISSING  {slug:58} (no live page) [{fname}]"))
        for fname, why in skipped:
            self.stdout.write(self.style.WARNING(f"skipped  {fname:58} ({why})"))

        self.stdout.write(self.style.NOTICE(
            f"\n{'DRY RUN — ' if dry else ''}{len(updated)} to update, "
            f"{len(unchanged)} unchanged, {len(missing)} missing, {len(skipped)} skipped"
        ))
