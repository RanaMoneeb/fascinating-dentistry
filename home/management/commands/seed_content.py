from django.core.management.base import BaseCommand
from wagtail.models import Site

from home.models import HomePage
from home.homepage_content import HERO_INTRO, META_TITLE, META_DESC
from blog.models import BlogIndexPage, BlogPage, Category

CATEGORIES = [
    ("Oral Hygiene", "oral-hygiene"),
    ("Cosmetic Dentistry", "cosmetic-dentistry"),
    ("Restorative Dentistry", "restorative-dentistry"),
]

POSTS = [
    {
        "title": "10 Essential Tips for Maintaining Healthy Teeth and Gums",
        "slug": "10-essential-tips-healthy-teeth-gums",
        "category": "oral-hygiene",
        "excerpt": "Discover the top daily habits and professional tips that can help you maintain optimal oral health.",
        "body": (
            "<p>Maintaining healthy teeth and gums is essential for your overall well-being.</p>"
            "<h2>1. Brush twice a day</h2><p>Brush with fluoride toothpaste for two minutes, twice a day.</p>"
            "<h2>2. Floss daily</h2><p>Flossing removes plaque between teeth where brushing can't reach.</p>"
            "<h2>3. Visit your dentist regularly</h2><p>Six-monthly check-ups catch problems early.</p>"
        ),
    },
    {
        "title": "The Complete Guide to Teeth Whitening Options",
        "slug": "complete-guide-teeth-whitening",
        "category": "cosmetic-dentistry",
        "excerpt": "From professional treatments to at-home remedies, explore all the teeth whitening options available.",
        "body": (
            "<p>A bright, white smile is something many people want.</p>"
            "<h2>Professional in-office whitening</h2><p>Uses stronger bleaching agents for fast results.</p>"
            "<h2>Take-home trays</h2><p>Custom trays from your dentist balance convenience and effectiveness.</p>"
        ),
    },
    {
        "title": "What to Expect During Your First Dental Implant Consultation",
        "slug": "first-dental-implant-consultation",
        "category": "restorative-dentistry",
        "excerpt": "Preparing for a dental implant consultation? Learn what questions to ask and what to expect.",
        "body": (
            "<p>Dental implants are a long-lasting solution for missing teeth.</p>"
            "<h2>Your medical history</h2><p>Your dentist reviews health factors that affect healing.</p>"
            "<h2>Imaging</h2><p>X-rays and 3D scans assess jawbone density.</p>"
            "<h2>Treatment plan</h2><p>You receive a personalised plan with timeline and costs.</p>"
        ),
    },
]


class Command(BaseCommand):
    help = "Seed the homepage + blog content."

    def handle(self, *args, **options):
        site = Site.objects.first()
        home = site.root_page.specific

        # Blog index (create first so the hero CTA can link to it)
        blog_index = BlogIndexPage.objects.child_of(home).first()
        if not blog_index:
            blog_index = BlogIndexPage(title="Blog", slug="blog")
            home.add_child(instance=blog_index)
        blog_index.intro = "<p>Explore our collection of dental health articles, tips, and guides.</p>"
        blog_index.save_revision().publish()
        self.stdout.write(self.style.SUCCESS("Blog index ready"))

        # Homepage
        home.title = "Fascinating Dentistry"
        home.hero_title = "Australia's Most Comprehensive Dental Resource"
        home.hero_subtitle = HERO_INTRO
        home.seo_title = META_TITLE
        home.search_description = META_DESC
        home.hero_cta_label = "Explore the blog"
        home.hero_cta_link = blog_index
        home.intro = (
            "<h2>Who we are</h2>"
            "<p>Fascinating Dentistry is Australia's independent dental information resource — a public "
            "directory of dental services, conditions, treatments, costs, and oral health data. We do not "
            "operate clinics, sell treatments, or rank providers for payment. Our content is written by "
            "Australian journalists and reviewed by AHPRA-registered dentists.</p>"
            "<h2>What we cover</h2>"
            "<p>We publish detailed guides across general, restorative, cosmetic, and orthodontic "
            "dentistry, plus dental implants, oral surgery, paediatric and specialist services — "
            "alongside transparent cost estimates from ADA fee surveys and condition guides for over "
            "50 oral health issues.</p>"
        )
        home.save_revision().publish()
        self.stdout.write(self.style.SUCCESS("Homepage seeded"))

        # Categories
        cats = {}
        for name, slug in CATEGORIES:
            obj, _ = Category.objects.get_or_create(slug=slug, defaults={"name": name})
            cats[slug] = obj

        # Posts
        for p in POSTS:
            bp = BlogPage.objects.child_of(blog_index).filter(slug=p["slug"]).first()
            if not bp:
                bp = BlogPage(title=p["title"], slug=p["slug"], excerpt=p["excerpt"], body=p["body"])
                bp.categories = [cats[p["category"]]]
                blog_index.add_child(instance=bp)
            else:
                bp.title = p["title"]
                bp.excerpt = p["excerpt"]
                bp.body = p["body"]
                bp.categories = [cats[p["category"]]]
            bp.save_revision().publish()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(POSTS)} blog posts"))
