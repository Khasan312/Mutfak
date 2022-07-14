from .base import *

SITE_ID = 1

AUTH_USER_MODEL = 'users.User'

# DATABASE CONFIGURATION ######################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mutfak_db',
        'USER': 'khasan',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hasan.ucuturkiye@gmail.com'
EMAIL_HOST_PASSWORD = 'tsattlxrisdlexds'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'