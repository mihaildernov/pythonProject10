"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_pjn=ky8=9+0#)h0b&34^gumiqwq)x4%qj&eer43j=s8+rl8gb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'appointments',
    'django_apscheduler',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'basic.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'localhost',
            'PASSWORD': 'Password for postgres user',
            'PORT': '5432',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

USE_I18N = True

USE_TZ = True

SITE_ID = 2

LOGIN_URL = 'sign/login/', '/accounts/login/'

LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'ya.dernov13'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True

ADMINS = [
    ('Mihail', 'mihaildernov@gmail.com'),
]

SERVER_EMAIL = 'ya.dernov13@yandex.ru'

DEFAULT_FROM_EMAIL = 'ya.dernov13@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_file': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s %(filename)s'
        },
        'errors_file': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s (exc_info) %(filename)s'
        },
        'main_console': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warning_console': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'error_console': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s} (exc_info)'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_console',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_console',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_console',
        },
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'main_file',
            'filename': 'general.log'
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'errors_file',
            'filename': 'errors.log'
        },
        'file_security': {
            'class': 'logging.FileHandler',
            'formatter': 'main_file',
            'filename': 'security.log'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning_console'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'file'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True,
        },
    }
}