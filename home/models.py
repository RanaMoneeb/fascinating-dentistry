from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel


class HomePage(Page):
    hero_title = models.CharField(
        max_length=255,
        default="Australia's Most Comprehensive Dental Resource",
    )
    hero_subtitle = models.TextField(blank=True)
    hero_cta_label = models.CharField(max_length=80, default="Explore the blog")
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    intro = RichTextField(
        blank=True,
        features=["h2", "h3", "p", "bold", "italic", "ul", "ol", "link"],
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_title"),
                FieldPanel("hero_subtitle"),
                FieldPanel("hero_cta_label"),
                PageChooserPanel("hero_cta_link"),
            ],
            heading="Hero",
        ),
        FieldPanel("intro", classname="full"),
    ]

    def get_context(self, request):
        from . import homepage_content
        from blog.models import BlogPage

        context = super().get_context(request)
        context["hp"] = homepage_content
        try:
            context["latest_posts"] = BlogPage.objects.live().order_by("-first_published_at")[:3]
        except Exception:
            context["latest_posts"] = []
        return context
