"""Wagtail signal handlers — clear the live-paths cache whenever a page is
published or unpublished so that all other pages immediately recognise new
(and removed) links via the |live_links / |live_html filters."""
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from wagtail.signals import page_published, page_unpublished

_CACHE_KEY = "home_live_rel_paths"


@receiver(page_published)
def _clear_on_publish(sender, instance, **kwargs):
    cache.delete(_CACHE_KEY)


@receiver(page_unpublished)
def _clear_on_unpublish(sender, instance, **kwargs):
    cache.delete(_CACHE_KEY)
