""" securite_root/auth_service/auth_service/settings.py
Django settings for auth_service project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from .routers import AuthRouter
from annuaire_root import *
from pathlib import Path
# auth_service/settings.py
DATABASE_ROUTERS = ['custom_auth_service.routers.AuthRouter']
ROOT_URLCONF = 'custom_auth_service.urls'

WSGI_APPLICATION = 'custom_auth_service.wsgi.application'

# Remplacez 'auth.User' par le chemin complet de votre modèle User personnalisé
AUTH_USER_MODEL = 'custom_auth_service.auth_db.User'
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_SERVICE_DATABASES = {
    'auth_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auth_db',  # Utilisez le nom de votre base de données
        'USER': 'root',
        'PASSWORD': 'shyrin12',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'unix_socket': '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
        },
    }
}