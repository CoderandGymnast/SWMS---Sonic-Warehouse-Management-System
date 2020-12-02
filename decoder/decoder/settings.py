"""
Django settings for decoder project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

from pathlib import Path

os.environ["eventlet.input"] = "EVENTLET"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# [LOG PID]:
PID = os.getpid()
print(f"Process ID '{PID}' - BASE_DIR '{BASE_DIR}'")  # Fork (System Call): https://en.wikipedia.org/wiki/Fork_(system_call)

# [GENERATE SHUTDOWN SCRIPT]:
f = open(f"{BASE_DIR}/shutdown.bat", 'w')
f.write(f"taskkill /F /PID {PID}")
f.close()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*g%#j+=m!(&!6x$*z6eg4xlr^-j4%fe8f6a2)z4y(#a4p6i8yi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Debug details in the browser.
# INFO = False
# WARNING = False
# ERROR = False
# CRITICAL = False

ALLOWED_HOSTS = ['*', ]

# ALLOWED_HOSTS = []  #  CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.

# Application definition

INSTALLED_APPS = [
	"qr_bar_decoder.apps.QrBarDecoderConfig",
	'django.contrib.admin',
	'django.contrib.auth',  # The core of authentication framework.
	'django.contrib.contenttypes',  # Permissions - Authorization.
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions across requests.
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'decoder.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'decoder.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

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

STATIC_URL = '/static/'

# LOGGING = {  # Reference: https://docs.djangoproject.com/en/1.8/topics/logging/.
# 	'version': 1,
# 	'disable_existing_loggers': True,
#
# 	'handlers': {
# 		'null': {
# 			'class': 'logging.NullHandler',
# 		},
# 	},
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # python manage.py collectstatic

# [IMAGES URL PATTERN]:
STATIC_IMAGES_URL_PATTERN = "/admin/img/"
STATIC_GIS_IMAGES_URL_PATTERN = "/admin/img/gis/"

# [OPEN CV CONFIGURATION]:
# FRAME_MAX_WIDTH = 280  # 1. Galaxy Fold. 2. The more image size, the more time consuming.
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480

# LOGIN_REDIRECT_URL = "/admin/"
LOGOUT_REDIRECT_URL = "/"

"""
[APPLICATION STATIC URL PATTERN]:
"""
APPLICATION_JS_URL_PATTERN = "/js/"
APPLICATION_JS_VENDOR_URL_PATTERN = "/js/vendor/"

