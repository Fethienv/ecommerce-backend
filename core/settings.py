"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*l_!4%di!7w3sgui-c^eac$f!mz$s=$tnk0u7hdy!#xy7)&=o6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['jawlatte.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

THEME_NAME = 'starship'
THEMES_DIR = 'themes'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR) + '/' + THEMES_DIR + '/' + THEME_NAME + '/templates', ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'ecommerce_backend_db',
        'HOST': "mongodb+srv://ecommerce_backend:29hhiQykG3Stqrpn@cluster0.wtb5y.mongodb.net/ecommerce_backend_db?retryWrites=true&w=majority",
        'PORT': 27017,
        'USER': 'ecommerce_backend',
        'PASSWORD': '29hhiQykG3Stqrpn',
    },
}

# Heroku postgresql
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd85hf0nimeug4t',
        'HOST': 'ec2-54-247-78-30.eu-west-1.compute.amazonaws.com',
        'PORT': 5432,
        'USER': 'fytiwucmgvxgas',
        'PASSWORD': '3b86f2983cd6889608bc471bc374c51a2182c5c94f95171b754d33d0f7a542f8',
        'CONN_MAX_AGE': 500,  # Heroku
    },
}
'''
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/' + THEMES_DIR + '/' + THEME_NAME + '/static/'
STATIC_ROOT = str(BASE_DIR) + '/' + THEMES_DIR + '/' + THEME_NAME + '/static'

# Heroku users
django_heroku.settings(locals())
