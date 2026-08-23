import re
from blog.models import BlogPage

posts = BlogPage.objects.live()
fixed_count = 0

for p in posts:
    schema = p.schema_json or ''
    changed = False

    # Fix /services/ links in schema
    if '/services/' in schema:
        schema = schema.replace('/services/endodontics/root-canal-therapy/', '/blog/endodontics/')
        schema = re.sub(r'/services/[^"]*', '/blog/endodontics/', schema)
        changed = True

    # Fix practice language in schema text fields
    if 'contact our clinic' in schema.lower():
        schema = re.sub(
            r'If you require treatment for an infected tooth, contact our clinic to schedule an appointment for [^"]*root canal therapy[^"]*',
            'For more information about root canal procedures, explore our comprehensive endodontics guides',
            schema, flags=re.IGNORECASE
        )
        schema = re.sub(
            r'If you require treatment[^"]*contact our clinic[^"]*',
            'For more information about root canal procedures, explore our comprehensive endodontics guides',
            schema, flags=re.IGNORECASE
        )
        schema = schema.replace('contact our clinic', 'consult a qualified dentist')
        changed = True

    if 'our clinic' in schema.lower():
        schema = schema.replace('our clinic', 'a qualified dentist')
        changed = True

    if changed:
        p.schema_json = schema
        p.save_revision().publish()
        fixed_count += 1
        print(f'FIXED SCHEMA: {p.slug}')

print(f'\nTotal schemas fixed: {fixed_count}')
