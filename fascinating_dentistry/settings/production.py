import os
from urllib.parse import urlparse
from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", os.environ.get("JWT_SECRET", "django-insecure-fallback-2026"))

# Parse DATABASE_URL from environment (set by Coolify)
_db_url = os.environ.get("DATABASE_URL", "")
if _db_url:
    _parsed = urlparse(_db_url)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": _parsed.path.lstrip("/"),
            "USER": _parsed.username,
            "PASSWORD": _parsed.password,
            "HOST": _parsed.hostname,
            "PORT": str(_parsed.port or 5432),
        }
    }

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL", "https://fascinatingdentistry.com")

STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Configure Whitenoise to serve media files as well
# In production, media files (uploaded images/documents) need to be accessible
WHITENOISE_MEDIA = True

try:
    from .local import *
except ImportError:
    pass
