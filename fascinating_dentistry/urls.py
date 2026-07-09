from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("sitemap.xml", sitemap, name="sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files in production
if not settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]

urlpatterns = urlpatterns + [
    path("", include(wagtail_urls)),
]
