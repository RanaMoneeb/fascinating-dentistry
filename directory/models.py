from wagtail.models import Page


class CountryHubPage(Page):
    """National directory hub / Top 10 listicle (e.g. /australia/ — 'Top 10 Dentists in
    Australia'). All content comes from directory.hub_content (transcribed from the source
    markdown); links to not-yet-built pages are neutralised at render via is_live_url."""

    def get_context(self, request):
        from . import hub_content

        context = super().get_context(request)
        context["hub"] = hub_content
        return context
