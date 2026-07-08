from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#+86*a*hcx2qhlv$h64@wr6%2kfq$$w@zyizq8d8l#8%-_#d@q"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# django-tailwind (dev only)
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
INTERNAL_IPS = ["127.0.0.1"]


try:
    from .local import *
except ImportError:
    pass
