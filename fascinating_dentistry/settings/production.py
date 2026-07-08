import os
from .base import *

DEBUG = False

# Served by Coolify's proxy (Traefik) — trust the proxy headers
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ALLOWED_HOSTS from environment (comma-separated), fallback to *
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Wagtail admin URL (for emails)
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", "https://fascinatingdentistry.com")

STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

try:
    from .local import *
except ImportError:
    pass
