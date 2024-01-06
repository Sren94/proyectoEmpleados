from .base import *
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbEmpleado',
        'USER':'stroop94',
        'PASSWORD':'Stroop94',
        'HOST':'localhost',
        'PORT':'5432',
        
}
}
STATIC_URL = 'static/'