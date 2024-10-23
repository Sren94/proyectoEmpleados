from .base import *
import os
import environ
import dj_database_url
# Cargar las variables de entorno
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Clave secreta y configuración de depuración
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

# Hosts permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=["localhost"])

# Orígenes de confianza para CSRF
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# Configuración de la base de datos
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )

}
#Carga De Archivos Estaticos
STATIC_URL = env('STATIC_URL')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

