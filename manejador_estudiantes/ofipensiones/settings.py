"""
Django settings for ofipensiones project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z1=7s_=_w%$dv)t0^22*uqx+nw=l7!c9r!-gy^nqjf2(%y+t!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestor_usuario_roles',
    'social_django',
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

ROOT_URLCONF = 'ofipensiones.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'ofipensiones', 'templates')],
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

WSGI_APPLICATION = 'ofipensiones.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'estudiante_db',
        'CLIENT': {
            'host': 'mongodb://estudiante_user:isis2503@10.128.0.82:27017',  # Dirección de MongoDB
            'username': 'estudiante_user',        # Usuario de MongoDB
            'password': 'isis2503',               # Contraseña de MongoDB
            'authSource': 'admin',                # Base de datos de autenticación
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# MongoDB Atlas Config
MONGO_CLI = "mongodb://estudiante_user:isis2503@10.128.0.82:27017"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://dev-2lbfseybkx5rveyk.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F34.173.96.78:8080"

SOCIAL_AUTH_TRAILING_SLASH = False  # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-2lbfseybkx5rveyk.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'EpWAnWYTXBLt32lHT0eSLe0sKH0aKvfz'
SOCIAL_AUTH_AUTH0_SECRET = 'wqrzQTFKdmKgJ_u0Yupwf75eh25EMSXWc5LueBzHuCheN8gVurfEQwpXChTKoT38'

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email',
    'role',
]

AUTHENTICATION_BACKENDS = {
    'ofipensiones.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
}

