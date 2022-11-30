import os
import sys

from settings.conf import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))



DJANGO_AND_THIRD_PARTY_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

PROJECT_APPS = [
    'products.apps.ProductsConfig',
]

SITE_ID = 1

INSTALLED_APPS = DJANGO_AND_THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['products/templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'deploy.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STRIPE_PUBLIC_KEY = 'pk_test_51M7BYcCOxFvNOMyPj8EahEVCzO7PtgI4sfiYrfsS2TZkyYVws9kgpt6U42X5wcK5Sno6VQZKyreIXy9QtagkiEWi00I1c9FJMI'
STRIPE_SECRET_KEY = 'sk_test_51M7BYcCOxFvNOMyPDD5Cxda4XXMMIXI1Rhh1If7i70o5IK0RTR9OBuUTJhkHQ4i5rh4EbaMjkTFHdVVdRiBsN2Y100UvbcW9pC'
STRIPE_WEBHOOK_SECRET = ''
