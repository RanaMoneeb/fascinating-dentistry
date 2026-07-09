from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.fields import RichTextField

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    credentials = models.CharField(max_length=500, blank=True)
    bio = models.TextField("Bio (HTML)", blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("credentials"),
        FieldPanel("bio"),
    ]

    class Meta:
        verbose_name_plural = "authors"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}{' - ' + self.credentials if self.credentials else ''}"


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    panels = [FieldPanel("name"), FieldPanel("slug")]

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "blog.BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    body = models.TextField("Body (HTML)", blank=True)
    schema_json = models.TextField("Schema.org JSON-LD", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
    ]

    def get_template(self, request, *args, **kwargs):
        from home.models import HomePage
        if isinstance(self.get_parent().specific, HomePage):
            return "blog/blog_index_page.html"
        return "blog/cluster_hub_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        from . import blog_hub_content
        context["bh"] = blog_hub_content
        # Posts in this cluster only
        context["posts"] = BlogPage.objects.descendant_of(self).live().order_by("-first_published_at")[:6]
        # For cluster hubs: process the body (numbered sections, TOC, dead-link neutralising)
        if self.body:
            from home.templatetags.home_tags import process_body
            import json as _json
            processed = process_body(self.body)
            context["body_html"] = processed["html"]
            context["toc"] = processed["toc"]
            try:
                context["schema_blocks"] = _json.loads(self.schema_json or "[]")
            except (ValueError, TypeError):
                context["schema_blocks"] = []
        return context


class BlogPage(Page):
    excerpt = models.CharField(max_length=500, blank=True)
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    author = models.ForeignKey(
        "blog.Author",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
    )
    body = RichTextField("Body", blank=True, features=["h2", "h3", "h4", "bold", "italic", "ol", "ul", "link", "image", "blockquote"])
    # Deprecated fields - kept for backward compatibility
    author_name = models.CharField(max_length=200, blank=True, editable=False)
    author_credentials = models.CharField(max_length=500, blank=True, editable=False)
    author_bio = models.TextField("Author Bio (HTML)", blank=True, editable=False)
    categories = ParentalManyToManyField("blog.Category", blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("excerpt"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("excerpt"),
        FieldPanel("cover_image"),
        FieldPanel("author"),
        FieldPanel("body", classname="full"),
        FieldPanel("categories"),
        FieldPanel("tags"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        from home.templatetags.home_tags import process_body
        processed = process_body(self.body or "")
        context["body_html"] = processed["html"]
        context["toc"] = processed["toc"]
        return context
