from .base import *
from pathlib import Path
import environ  # <-- Updated!
environ.Env.read_env(BASE_DIR / '.env')  # <-- Updated!
env = environ.Env(  # <-- Updated!
    # set casting, default value
    DEBUG=(bool, False),
)
SECRET_KEY = env('SECRET_KEY')  # <-- Updated!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') 

DEBUG = True
import os
ALLOWED_HOSTS = []
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #}
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME':'dbEmpleado',
#        'USER':'stroop94',
#        'PASSWORD':'Stroop94',
#        'HOST':'localhost',
#        'PORT':'5432',
#        
#}  
environ.Env.read_env(BASE_DIR / '.env')  # <-- Updated!
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

environ.Env.read_env(BASE_DIR / '.env')  # <-- Updated!