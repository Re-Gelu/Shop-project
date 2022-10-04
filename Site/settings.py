"""
Django settings for Site project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy
import os

# Base admin settings
ADMIN_SETTINGS = {
    'SITE_NAME': 'SAMPLE-SHOP.COM',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$aqn(bz0br&rqn0%)-#wi@g!w14h55*zr4&_y_v=)5ajo$75j_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'admin_interface',
    'colorfield',
    'filebrowser',
    'tinymce',
    'extra_settings',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'django_celery_results',
    
    'Shop',
    'Cart',
    'Orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
]

ROOT_URLCONF = 'Site.urls'

TEMPLATE_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Site.context_processors.admin_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'Site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

""" 'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } """
    
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Prod settings

if os.environ.get("DEBUG"):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = int(os.environ.get("DEBUG", default=0))

    # 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
    # For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
    ALLOWED_HOSTS = str(os.environ.get("DJANGO_ALLOWED_HOSTS")).split(" ")

# Login settings

LOGIN_REDIRECT_URL = reverse_lazy('dashboard')

LOGIN_URL = reverse_lazy('login')

LOGOUT_URL = reverse_lazy('logout')

# Session settings

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

CART_SESSION_ID = 'cart'

# Cart settings

MAX_PRODUCT_AMOUNT_IN_CART = 10

MIN_PRODUCT_AMOUNT_IN_CART = 1

MAX_PRODUCTS_IN_CART = 5

MIN_PRODUCTS_IN_CART = 1

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

# Celery settings
CELERY_CACHE_BACKEND = 'default'

""" # Grappelli settings

GRAPPELLI_ADMIN_TITLE = 'Админка сайта ' + ADMIN_SETTINGS['SITE_NAME']

GRAPPELLI_SWITCH_USER = True

GRAPPELLI_INDEX_DASHBOARD = 'Site.dashboard.CustomIndexDashboard' """

# Filebrowser settings

FILEBROWSER_DIRECTORY = ''

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Миниатюра (1 кол.)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Маленькая (2 кол.)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Средняя (4 кол.)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Большая (6 кол.)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Огромная (8 кол.)', 'width': 680, 'height': '', 'opts': ''},
}

# 'Extra settings' settings

EXTRA_SETTINGS_ENFORCE_UPPERCASE_SETTINGS = True

EXTRA_SETTINGS_CACHE_NAME = 'default'

EXTRA_SETTINGS_SHOW_TYPE_LIST_FILTER = True

EXTRA_SETTINGS_SHOW_NAME_PREFIX_LIST_FILTER = True

EXTRA_SETTINGS_FILE_UPLOAD_TO = "media/files/"

EXTRA_SETTINGS_IMAGE_UPLOAD_TO = "media/files/"

EXTRA_SETTINGS_VERBOSE_NAME = "Настройки проекта"

EXTRA_SETTINGS_DEFAULTS = [
    {
        "name": "SITE_NAME",
        "type": "string",
        "value": "Настройте параметр SITE_NAME",
        "description": "Название сайта",
    },
    {
        "name": "EMAIL_1",
        "type": "string",
        "value": "Настройте параметр EMAIL_1",
        "description": "Email 1 для контактов",
    },
    {
        "name": "EMAIL_2",
        "type": "string",
        "value": "Настройте параметр EMAIL_2",
        "description": "Email 2 для контактов (опционально)",
    },
    {
        "name": "PHONE_NUMBER_1",
        "type": "string",
        "value": "Настройте параметр PHONE_NUMBER_1",
        "description": "Номер телефона 1 для контактов",
    },
    {
        "name": "PHONE_NUMBER_2",
        "type": "string",
        "value": "Настройте параметр PHONE_NUMBER_2",
        "description": "Номер телефона 2 для контактов (опционально)",
    },
    {
        "name": "CONTACTS_PAGE_INFORMATION",
        "type": "text",
        "value": "Настройте параметр CONTACTS_PAGE_INFORMATION",
        "description": "Информация на странице 'Контакты'",
    },
    {
        "name": "LOCATION",
        "type": "text",
        "value": "Настройте параметр LOCATION",
        "description": "Местоположение организации",
    },
    {
        "name": "LOCATION_MAP_HTML",
        "type": "text",
        "value": "Настройте параметр LOCATION_MAP_HTML",
        "description": "HTML код карты. Получить код можно по ссылкам: https://yandex.ru/map-constructor/ , https://makemap.2gis.ru/ , https://www.google.com/intl/ru/maps/about/mymaps/",
    },
    {
        "name": "ABOUT_PAGE_INFORMATION",
        "type": "text",
        "value": "Настройте параметр ABOUT_PAGE_INFORMATION",
        "description": "Информация на странице 'О нас'",
    },
    {
        "name": "MAIN_COLOR",
        "type": "string",
        "value": "#dc143c",
        "description": "Основной цвет в дизайне сайта",
    },
    {
        "name": "SECOND_MAIN_COLOR",
        "type": "string",
        "value": "#dc143c",
        "description": "Второй основной цвет в дизайне сайта",
    },
    {
        "name": "SECOND_MAIN_COLOR_O",
        "type": "string",
        "value": "rgba(220, 20, 60, 0.9)",
        "description": "Второй основной цвет в дизайне сайта с прозрачностью (рекомендуется 0.9)",
    },
    {
        "name": "SHADOW_COLOR",
        "type": "string",
        "value": "rgba(220, 20, 60, 0.5)",
        "description": "Цвет теней в дизайне сайта с прозрачностью (рекомендуется 0.5)",
    },
    {
        "name": "A_TEXT_COLOR",
        "type": "string",
        "value": "#dc143c",
        "description": "Основной цвет ссылок в дизайне сайта",
    },
]

# Django-admin-interface settings

X_FRAME_OPTIONS = "SAMEORIGIN"

SILENCED_SYSTEM_CHECKS = ["security.W019"]