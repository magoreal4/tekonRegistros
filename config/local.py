from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n2_ug(0q%+)9(a@nzw#bn%+wf@5d)0^c&cm!zm7ozy(j08hc%@"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    # "django_extensions",
    # 'django_browser_reload',
    'theme',
    # "debug_toolbar",
    ]  # noqa: F405

MIDDLEWARE += [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]  # noqa: F405

INTERNAL_IPS = [
    "127.0.0.1",
]