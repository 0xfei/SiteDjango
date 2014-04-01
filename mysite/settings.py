"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
MEDIA_ROOT = SITE_ROOT
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
DATA_ROOT = os.path.join(SITE_ROOT, 'data/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#agm-@c_^badm)hzj+k#%(mt1&2ae#8v21#36^&5k*m7lpae@o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
)


STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'static/'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'default',
    'blog',
    'ustvs',
    'words',
    'tinymce',
    'django.contrib.admin',
    'embed_video',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ADMINS = (
    ('0x01f', '0x01f@163.com'),
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_ROOT, '1.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
DEFAULT_CHARSET = 'UTF-8'

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'width': 1000,
    'height': 600,
}
