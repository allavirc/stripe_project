from . import get_env_variable


SECRET_KEY = get_env_variable("SECRET_KEY")

DEBUG = get_env_variable("DEBUG")

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'settings.urls'

