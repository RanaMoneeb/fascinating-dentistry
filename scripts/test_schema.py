"""
Schema validation script — checks that every page's JSON-LD is valid.

Run: python manage.py shell -c "exec(open('scripts/test_schema.py').read())"

Or: python scripts/test_schema.py (standalone, connects to the live site)
"""
import json
import urllib.request
import sys

BASE_URL = "https://fascinatingdentistry.com"

PAGES = [
    "/",
    "/blog/",
    "/blog/endodontics/",
    "/blog/endodontics/what-is-root-canal-therapy/",
    "/australia/",
    "/about/",
    "/methodology/",
    "/editorial-team/",
    "/editorial-team/dr-anthony-au/",
    "/medical-review/",
    "/medical-reviewers/",
    "/editorial-policy/",
    "/corrections/",
    "/disclosures/",
    "/privacy/",
    "/terms/",
    "/contact/",
]

import re

def extract_json_ld(html):
    """Extract all JSON-LD blocks from HTML."""
    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    return re.findall(pattern, html, re.DOTALL)

def check_page(url):
    """Check a page for valid JSON-LD and SEO tags."""
    issues = []
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SchemaBot/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")

        # Check JSON-LD blocks
        blocks = extract_json_ld(html)
        if not blocks:
            issues.append("NO JSON-LD found")
        else:
            for i, block in enumerate(blocks):
                try:
                    data = json.loads(block)
                except json.JSONDecodeError as e:
                    issues.append(f"Invalid JSON-LD block {i+1}: {str(e)[:80]}")

        # Check canonical
        if '<link rel="canonical"' not in html:
            issues.append("Missing canonical URL")

        # Check meta description
        if '<meta name="description"' not in html:
            issues.append("Missing meta description")

        # Check Open Graph
        if 'property="og:title"' not in html:
            issues.append("Missing og:title")
        if 'property="og:description"' not in html:
            issues.append("Missing og:description")

        # Check Twitter Card
        if 'name="twitter:card"' not in html:
            issues.append("Missing twitter:card")

        return len(blocks), issues
    except Exception as e:
        return 0, [f"Request failed: {str(e)[:80]}"]

def main():
    print(f"Schema & SEO audit — {BASE_URL}")
    print("=" * 60)
    total_issues = 0
    for path in PAGES:
        url = BASE_URL + path
        count, issues = check_page(url)
        status = "✅" if not issues else "❌"
        print(f"\n{status} {path}")
        print(f"   JSON-LD blocks: {count}")
        for issue in issues:
            print(f"   ⚠️  {issue}")
            total_issues += 1

    print(f"\n{'=' * 60}")
    if total_issues == 0:
        print("ALL CHECKS PASSED ✅")
    else:
        print(f"{total_issues} issues found")

if __name__ == "__main__":
    main()
