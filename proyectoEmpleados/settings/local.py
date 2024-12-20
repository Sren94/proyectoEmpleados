from .base import *
from pathlib import Path
import environ  # <-- Updated!

import os

environ.Env.read_env(BASE_DIR / '.env')  # <-- Updated!
env = environ.Env(  # <-- Updated!
    # set casting, default value
    DEBUG=(bool, False),
)
SECRET_KEY = env('SECRET_KEY')  # <-- Updated!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') 

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':env('NAME_DATABASE'),
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASSWORD'),
        'HOST':env('DB_HOST'),
        'PORT':'5432',
    }
}
#aqui se registra para la creacion de archivos estaticos
#como css,js etc 
#y sirve para obtener y direccionar los recursos 
#para el proyecto
STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, "static")]

#aqui se da registro de los archivos media 
#y esto sirve para direccionar los recursos
#se deben de registrar en esta carpeta
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

