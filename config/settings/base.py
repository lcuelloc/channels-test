"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import environ


ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('v1')

env = environ.Env()
env.read_env(str(ROOT_DIR.path('.env')))

# KEY
# -------------------------------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY')

# SITE CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# APP CONFIG
# -------------------------------------------------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_extensions',
    'expander',
    'corsheaders',
]

LOCAL_APPS = [
    'v1.accounts.apps.AccountsConfig',
]

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

DEBUG = env.bool('DEBUG', False)

# AUTH USER MODEL
# -------------------------------------------------------------------------------------------------
AUTH_USER_MODEL = 'accounts.User'

# MIDDLEWARES
# -------------------------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Cors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL')
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

ROOT_URLCONF = 'config.urls'

# CORS
# -------------------------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'content-disposition',
    'cache-control',
]

# EXPAND QUERIES
# -------------------------------------------------------------------------------------------------
DRF_EXPANDER_EXPAND_ARG = 'expand'

# GENERAL CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.0/topics/i18n/
TIME_ZONE = 'America/Santiago'
LANGUAGE_CODE = 'es-cl'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


# TEMPLATE CONFIG
# -------------------------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(ROOT_DIR.path('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# STATICFILES CONFIG
# -------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR.path('static'))

STATICFILES_DIRS = [str(APPS_DIR.path('static')), ]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'