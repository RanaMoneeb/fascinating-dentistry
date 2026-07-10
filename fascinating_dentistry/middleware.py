"""Project-level middleware."""
from django.http import HttpResponsePermanentRedirect


class WwwToNonWwwRedirectMiddleware:
    """Permanently redirect ``www.<host>`` to ``<host>``.

    Coolify/Traefik is configured to serve both ``fascinatingdentistry.com`` and
    ``www.fascinatingdentistry.com`` to the app. This canonicalises every URL to
    the non-www host so there is a single indexable origin (Search Console
    friendly, avoids duplicate-content across hosts).

    Only acts when the request host begins with ``www.``; scheme, path and query
    string are preserved. Production detects HTTPS via
    ``SECURE_PROXY_SSL_HEADER`` (X-Forwarded-Proto set by Traefik), so the
    redirect target stays on https. No-op in local dev (host is localhost).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().lower()
        if host.startswith("www."):
            new_host = host[4:]  # strip the leading "www."
            scheme = "https" if request.is_secure() else "http"
            return HttpResponsePermanentRedirect(
                f"{scheme}://{new_host}{request.get_full_path()}"
            )
        return self.get_response(request)
