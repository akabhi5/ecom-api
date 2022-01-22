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
