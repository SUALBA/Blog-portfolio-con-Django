"""
Django settings for config project.

Proyecto profesional de Blog + Portfolio hecho con Django 5.2.

Autor: [Su Alba]
Fecha: 2025
"""

import os
from pathlib import Path
import dj_database_url

# === BASE DIRECTORY ===
BASE_DIR = Path(__file__).resolve().parent.parent


# === SECURITY CONFIGURATION ===
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu_clave_de_desarrollo')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'sualba.dev',
    'www.sualba.dev',
    'blog-sualba.onrender.com',
    'localhost',
    '127.0.0.1',
]


# === INSTALLED APPS ===
INSTALLED_APPS = [
     'admin_interface',
    'colorfield',  # Requerido por admin_interface
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Tu aplicación principal
]


# === MIDDLEWARE CONFIGURATION ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Sirve archivos estáticos directamente
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# === URLS CONFIGURATION ===
ROOT_URLCONF = 'config.urls'


# === TEMPLATES CONFIGURATION ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes agregar aquí carpetas personalizadas de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# === WSGI APPLICATION ===
WSGI_APPLICATION = 'config.wsgi.application'


# === DATABASE CONFIGURATION ===
# Usamos dj-database-url para conectar automáticamente a PostgreSQL en Render
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://blog_sualba_db_user:FrEsdgpkfkv4dCALvCk59AnAXhqwtpVO@dpg-d06nvtili9vc73eipf70-a/blog_sualba_db',
        conn_max_age=600,
        ssl_require=True
    )
}


# === PASSWORD VALIDATION ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# === INTERNATIONALIZATION ===
LANGUAGE_CODE = 'es-es'  # Español, porque somos de espíritu hispano 💪
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# === STATIC FILES CONFIGURATION ===
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise se encargará de servir los archivos estáticos en producción.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# === MEDIA FILES (Si algún día subes imágenes, CVs, etc.) ===
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# === DEFAULT AUTO FIELD ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

