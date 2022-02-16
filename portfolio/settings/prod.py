from .base import *

import cloudinary

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ['korededavid.herokuapp.com']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware', )

# Updated Installed apps
INSTALLED_APPS += ['cloudinary_storage', 'cloudinary', ]

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
# cloudinary.config(
#     upload_prefix=os.environ.get('CLOUD_UPLOAD_PREFIX'),
#     cloud_name=os.environ.get('CLOUD_NAME'),
#     api_key=os.environ.get('CLOUD_KEY'),
#     api_secret=os.environ.get('CLOUD_SECRET'),
#     secure=True
# )

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SERVER_EMAIL = os.environ.get('SERVER_EMAIL')
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = [
    ('KoredePortfolio', os.environ.get('EMAIL')),
]

MANAGERS = ADMINS

import dj_database_url

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
