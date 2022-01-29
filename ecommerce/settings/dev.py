from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-3)xnjni*hdrvvq#dybrn$y6lugk$&)x8qa4-xiz6#)eu+)4k@8'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    INTERNAL_IPS = ['127.0.0.1', ]

    # without this django debug toolbar not wroking
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
