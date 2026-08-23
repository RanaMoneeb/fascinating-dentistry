import re
from blog.models import BlogPage

posts = BlogPage.objects.live()
fixed_count = 0

for p in posts:
    body = p.body or ''
    changed = False

    # 1. Replace /services/ links with blog cluster link
    if '/services/' in body:
        # First handle the specific root-canal-therapy link
        body = body.replace(
            '<a href="/services/endodontics/root-canal-therapy/">root canal therapy</a>',
            '<a href="/blog/endodontics/">endodontics guides</a>'
        )
        # Then strip any remaining /services/ links
        body = re.sub(r'<a href="/services/[^"]*">([^<]+)</a>', r'\1', body)
        changed = True

    # 2. Fix "contact our clinic to schedule an appointment" practice language
    if 'contact our clinic' in body.lower():
        body = re.sub(
            r'If you require treatment for an infected tooth, contact our clinic to schedule an appointment for <a href="[^"]*">endodontics guides</a>\.',
            'For more information about root canal procedures, explore our comprehensive <a href="/blog/endodontics/">endodontics guides</a>.',
            body, flags=re.IGNORECASE
        )
        body = re.sub(
            r'contact our clinic to schedule an appointment for <a href="[^"]*">([^<]+)</a>',
            r'explore our <a href="/blog/endodontics/">endodontics guides</a>',
            body, flags=re.IGNORECASE
        )
        body = body.replace('contact our clinic', 'consult a qualified dentist')
        changed = True

    # 3. Fix remaining "our clinic"
    if 'our clinic' in body.lower():
        body = body.replace('our clinic', 'a qualified dentist')
        changed = True

    if changed:
        p.body = body
        p.save_revision().publish()
        fixed_count += 1
        print(f'FIXED: {p.slug}')

print(f'\nTotal fixed: {fixed_count}')
