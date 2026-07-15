"""Create ServiceListiclePage entries for directory service modules.

The content modules in directory/services/*.py define the page content,
but Wagtail needs actual page objects in its tree to serve them.
This command creates ServiceListiclePage entries under the Australia hub."""

import importlib
from django.core.management.base import BaseCommand
from wagtail.models import Page

from directory.models import ServiceListiclePage


class Command(BaseCommand):
    help = "Create ServiceListiclePage entries for directory service modules"

    def handle(self, *args, **options):
        # Find the Australia hub page
        australia = Page.objects.filter(slug="australia").first()
        if not australia:
            self.stdout.write(self.style.ERROR("Australia hub page not found. Run seed_pages first."))
            return

        australia = australia.specific

        # List of service modules to create
        services = [
            ("emergency-dentist", "emergency_dentist"),
            ("after-hours-dentist", "after_hours_dentist"),
        ]

        for slug, module_name in services:
            # Check if page already exists
            existing = ServiceListiclePage.objects.child_of(australia).filter(slug=slug).first()
            if existing:
                self.stdout.write(f"  exists: /australia/{slug}/")
                continue

            # Import the content module
            try:
                mod = importlib.import_module(f"directory.services.{module_name}")
            except ImportError as e:
                self.stdout.write(self.style.WARNING(f"  skipped: {module_name} — {e}"))
                continue

            # Create the page
            page = ServiceListiclePage(
                title=mod.H1,
                slug=slug,
                seo_title=mod.META_TITLE,
                search_description=mod.META_DESC,
            )

            australia.add_child(instance=page)
            page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS(f"  created: /australia/{slug}/"))

        self.stdout.write(self.style.SUCCESS("Done"))
