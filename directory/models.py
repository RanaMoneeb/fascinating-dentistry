import importlib

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


class ServiceListiclePage(Page):
    """A Top 10 service listicle under a country/city hub (e.g.
    /australia/emergency-dentist/). Content comes from directory.services.<slug>
    (slug "emergency-dentist" -> module "emergency_dentist"), mirroring the
    CountryHubPage + hub_content pattern. SEO title/description are kept in sync
    from content/*.md by the sync_meta command. Links to not-yet-built pages are
    neutralised at render via is_live_url; all outbound practice links are nofollow."""

    def get_context(self, request):
        context = super().get_context(request)
        try:
            context["s"] = importlib.import_module(
                "directory.services." + self.slug.replace("-", "_"))
        except ModuleNotFoundError:
            context["s"] = None
        return context

