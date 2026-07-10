"""Convert the live /contact/ page from ContentPage to ContactPage so the
contact form renders, and fix the placeholder email/address/ABN in its body.

Runs automatically on deploy (Coolify runs `manage.py migrate`). Idempotent.
"""
from django.db import migrations

EMAIL_OLD = "[email protected]"
EMAIL_NEW = "info@fascinatingdentistry.com"
ADDRESS = "Level 14, 320 Adelaide Street, Brisbane QLD 4000"
ABN = "71 482 937 615"


def fix_body(body):
    body = body or ""
    body = body.replace(EMAIL_OLD, EMAIL_NEW)
    body = body.replace("[Postal Address Placeholder]", ADDRESS)
    body = body.replace("[ABN Placeholder]", ABN)
    return body


def convert_contact_page(apps, schema_editor):
    ContentPage = apps.get_model("pages", "ContentPage")
    ContactPage = apps.get_model("pages", "ContactPage")

    # Idempotent: nothing to do if /contact/ is already a ContactPage.
    if ContactPage.objects.filter(slug="contact").exists():
        return

    old = ContentPage.objects.filter(slug="contact").first()
    if old is None:
        return  # Fresh database — seed_pages will create it as a ContactPage.

    parent = old.get_parent()

    new = ContactPage(
        title=old.title,
        slug="contact",
        body=fix_body(old.body),
        seo_title=old.seo_title,
        search_description=old.search_description,
    )

    # Delete the old ContentPage first to free the "contact" slug (unique per
    # sibling). This runs inside the migration transaction, so any failure
    # rolls the delete back too — the page is never lost.
    old.delete()
    parent.add_child(instance=new)
    new.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0004_contactsubmission"),
    ]
    operations = [
        migrations.RunPython(convert_contact_page, migrations.RunPython.noop),
    ]
