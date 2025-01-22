# ------------------------------------12.11.2024-----------------------------------
import pymysql

pymysql.install_as_MySQLdb()
from dotenv import load_dotenv  # Laden von Umgebungsvariablen
from pathlib import Path

load_dotenv()
import os
from datetime import timedelta

# Definiere das Basisverzeichnis des Projekts
BASE_DIR = Path(__file__).resolve().parent.parent

# Schnellstart-Entwicklungs-Einstellungen - nicht geeignet für die Produktion
# Siehe https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
# SICHERHEITSHINWEIS: Bewahren Sie den geheimen Schlüssel für die Produktion geheim!
# SICHERHEITSHINWEIS: Führen Sie das Projekt nicht mit aktiviertem Debug-Modus in der Produktion aus!
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'  # Debug-Modus aus den Umgebungsvariablen
ALLOWED_HOSTS = ['*']  # Erlaube allen Hosts den Zugriff auf das Projekt

# Anwendungskonfiguration

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rental',
    'user.apps.UserConfig',
    'booking',
    'listings',
    'search',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_extensions',
    'drf_yasg',  # API-Dokumentation http://127.0.0.1:8000/swagger/   http://127.0.0.1:8000/redoc/
]

# Middleware, die im Projekt verwendet wird
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rental.wsgi.application'

# BrowsableAPIRenderer ist in Django REST framework integriert und ermöglicht das Testen
# von API-Anfragen im Browser ohne zusätzliche Installationen

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Datenbank
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# --------------------------------------sqlite3------------------------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# -------------------------------------DATABASES----------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'ssl': {
                'check_hostname': False,  # Deaktivierung der Hostnamenüberprüfung
            },
        },
    }
}

# Passwortvalidierung
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Angabe des benutzerdefinierten Benutzermodells
AUTH_USER_MODEL = 'user.CustomUser'

# Standard-Django-Authentifizierungsbackend
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Einstellungen für die Simple JWT-Bibliothek-----------------------------------------------------------------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),  # Lebensdauer des Access-Tokens (in Minuten)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),  # Lebensdauer des Refresh-Tokens (in Tagen)
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=180),  # Lebensdauer des gleitenden Access-Tokens
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=5),  # Lebensdauer des gleitenden Refresh-Tokens
}

# Internationalisierung
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Statische Dateien (CSS, JavaScript, Bilder)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Standard-Primärschlüssel-Feldtyp
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
