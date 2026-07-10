import json

from django import forms
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import render

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class ContentPage(Page):
    """A designed content page (about, methodology, privacy, terms, etc.)."""

    body = models.TextField("Body (HTML)", blank=True)
    schema_json = models.TextField("Schema.org JSON-LD (JSON list)", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        from home.templatetags.home_tags import process_body

        processed = process_body(self.body or "")
        context["body_html"] = processed["html"]
        context["toc"] = processed["toc"]
        try:
            context["schema_blocks"] = json.loads(self.schema_json or "[]")
        except (ValueError, TypeError):
            context["schema_blocks"] = []
        return context


class ContactSubmission(models.Model):
    """Stores contact-form submissions so messages are captured even
    before SMTP/email is configured (viewable in the Wagtail admin)."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField(label="Your email")
    subject = forms.CharField(max_length=200, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")


class ContactPage(Page):
    """Contact page with a working form. Submissions are emailed to
    info@fascinatingdentistry.com (console backend in dev)."""

    body = models.TextField("Body (HTML)", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]

    def serve(self, request):
        sent = False
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                # Persist the submission so it is never lost, even when
                # SMTP/email is not yet configured.
                ContactSubmission.objects.create(
                    name=data["name"],
                    email=data["email"],
                    subject=data["subject"],
                    message=data["message"],
                )
                send_mail(
                    data["subject"],
                    f"From: {data['name']} <{data['email']}>\n\n{data['message']}",
                    data["email"],
                    ["info@fascinatingdentistry.com"],
                    fail_silently=True,
                )
                sent = True
                form = ContactForm()
        else:
            form = ContactForm()
        from home.templatetags.home_tags import process_body
        processed = process_body(self.body or "")
        return render(request, "pages/contact_page.html", {
            "page": self, "form": form, "sent": sent,
            "body_html": processed["html"],
            "toc": processed["toc"],
        })
