"""
Django settings for online_shop project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from decouple import config
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)  # True or False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'admin_honeypot',
    "azbankgateways",

    'carts',
    'category',
    'store',
    'accounts',
    'orders',
    'connect',
    'discount',
    'coupons',
    'like',

]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

SESSION_EXPIRE_SECONDS = config('SESSION_EXPIRE_SECONDS', cast=int)  # 1 week
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = config(
    'SESSION_EXPIRE_AFTER_LAST_ACTIVITY', cast=bool)
SESSION_TIMEOUT_REDIRECT = config('SESSION_TIMEOUT_REDIRECT')


ROOT_URLCONF = 'online_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_shop.wsgi.application'
# COSTUMIZING USER MODEL AUTHONTICATION
AUTH_USER_MODEL = 'accounts.Account'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'static'

# media files configurations
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# STATICFILES_DIRS = [os.path.join(BASE_DIR , 'static'),]

# SMTP CONFIGURATION
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        'ZARINPAL': {
            # 'MERCHANT_CODE': 'c9f5d404-1e0f-42d4-9a0d-b17e2e3700c3',
            # 'MERCHANT_CODE': '92d1635b-4155-4d64-8bdc-87e89755ea6b',
            'MERCHANT_CODE': '9a668b46-5577-4561-93a8-b24ac3a9d24d',
            'METHOD': 'POST',  # GET or POST
            'SANDBOX': 1,  # 0 disable, 1 active
        },
        'IDPAY': {
            'MERCHANT_CODE': 'ced73ac8-9ec9-40e6-aa47-08757df1be16',
            'METHOD': 'POST',  # GET or POST
            'X_SANDBOX': 1,  # 0 disable, 1 active
        },
    },
    'IS_SAMPLE_FORM_ENABLE': False,  # disable sample form
    'DEFAULT': 'IDPAY',  # set IDPay as the default gateway
    'CURRENCY': 'IRR',  # set the currency
    'TRACKING_CODE_QUERY_PARAM': 'tc',  # tracking code query parameter
    'TRACKING_CODE_LENGTH': 16,  # tracking code length
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',
    'BANK_PRIORITIES': [
        'ZARINPAL',
    ],  # IDPay priority
    'IS_SAFE_GET_GATEWAY_PAYMENT': True,  # enable secure payment
    'CUSTOM_APP': None,  # optional
}