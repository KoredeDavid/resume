from .base import *

import cloudinary

BASE_DIR = os.getcwd()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ['korededavid.herokuapp.com', 'korededavid.com', 'www.korededavid.com']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware', )

# Updated Installed apps
INSTALLED_APPS += ['cloudinary_storage', 'cloudinary', ]

# DATABASE settings uses sqlite when sqlite is set to true but uses Postgres if not
sqlite = os.environ.get('DATABASE', 'sqlite') == 'sqlite'

if sqlite:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DBNAME'),
            'USER': os.environ.get('DBUSER'),
            'PASSWORD': os.environ.get('DBPASS'),
            'HOST': os.environ.get('DBHOST'),
            'PORT': os.environ.get('DBPORT'),
        }
    }

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary_storage stuff
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUD_KEY'),
    'API_SECRET': os.environ.get('CLOUD_SECRET'),
}

# cloudinary stuff
cloudinary.config(
    upload_prefix=os.environ.get('CLOUD_UPLOAD_PREFIX'),
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

EMAIL_HOST = os.environ.get('EMAIL_HOST')  # The host to use for sending email.
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # Username to use for the SMTP server defined in EMAIL_HOST.
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # Password to use for the SMTP server defined in EMAIL_HOST
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SERVER_EMAIL = os.environ.get(EMAIL_HOST_USER)
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = [
    ('KoredePortfolio', EMAIL_HOST_USER),
]

MANAGERS = ADMINS


CORS_ALLOWED_ORIGINS = [
    "https://iamadesua.netlify.app",
    "http://iamadesua.netlify.app",
]


# Allows error log to be shown in console when Debug = False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}


if not sqlite:
    import dj_database_url

    prod_db = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(prod_db)
