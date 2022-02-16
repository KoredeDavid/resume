from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8%h+)yffuk&=5^jt*m-p4tyb%+!qoy486ljsl@tjei9t1elk)f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_DIR = os.getcwd()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SERVER_EMAIL = 'test@portfolio.com'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = [
    ('TeamPortfolio', 'test@portfolio.com'),
]

MANAGERS = ADMINS

