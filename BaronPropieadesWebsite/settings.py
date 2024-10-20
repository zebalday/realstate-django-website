"""
Django settings for BaronPropieadesWebsite project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os
import pymysql
import dotenv


# Load env variables
dotenv.load_dotenv()

# MySQL Installation
pymysql.install_as_MySQLdb()


# Set language to spanish
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]
LANGUAGE_CODE = 'es'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]
#ALLOWED_HOSTS = ["https://baronpropiedades.cl","baronpropiedades.cl"]

# Application definition
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "ckeditor",
    "BaronPropiedades",
    "phonenumber_field",
    "fontawesomefree"
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'BaronPropieadesWebsite.urls'
#ROOT_URLCONF = 'BaronPropiedadesWebsite.urls'

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

WSGI_APPLICATION = 'BaronPropieadesWebsite.wsgi.application'
#WSGI_APPLICATION = 'BaronPropiedadesWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST':'localhost',
        'PORT':'3306'
    }
} """

# Mail sending information
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/staticfiles/'


""" 
STATIC_ROOT = os.getenv('STATIC_ROOT')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.getenv('MEDIA_ROOT')
MEDIA_URL='/media/' 
"""


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media storage path
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL = "/media/"

# Ckeditor configs
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', 'Image', 'Table']
        ]
    }
}
