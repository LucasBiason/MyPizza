import os, datetime, json
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#hh^a@x8jf0*zftmhtzqwlrb8i+dlvxldiqlp0e&6jf=w^3u-$'

DEBUG = os.environ.get('DEBUG') or config('DEBUG') or False

ALLOWED_HOSTS = [ os.environ.get('ALLOWED_HOSTS') or config('ALLOWED_HOSTS') or '*']

SITE_ID = 1

AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
    'corsheaders',

    'src',
    'pizza',
    'users',
    'authentication',
]

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DB_HOST') or config('DB_HOST') or 'localhost',
        'NAME': os.environ.get('DB_NAME') or config('DB_NAME'),
        'USER': os.environ.get('DB_USER') or config('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS') or config('DB_PASS'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': json.loads(
            os.getenv('DATABASE_OPTIONS', '{}')
        ),
        'TEST': {
            'NAME': 'test_' + config('DB_NAME'),
            'MIRROR': 'default',
        }
    }
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


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

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = '/vol/web/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/vol/web/media'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'authentication.authentication.ExpiringTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'EXCEPTION_HANDLER':  'src.handler.api_exception_handler'
}

TOKEN_EXPIRE_TIME=datetime.timedelta(hours=1)


CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_WHITELIST') or config('CORS_WHITELIST') or ''
if not CORS_ORIGIN_WHITELIST:
    CORS_ORIGIN_WHITELIST = [
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]
if isinstance(CORS_ORIGIN_WHITELIST, str):
    CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST.split(',')


CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'DELETE',
]


CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'Authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
