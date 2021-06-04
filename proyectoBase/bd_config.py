import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open("connection.json") as f:
    secret = json.loads(f.read())

def get_data(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)

SECRET_KEY = get_data('SECRET_KEY')

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_data('BD_NAME'),
        'USER': get_data('USUARIO'),
        'PASSWORD':get_data('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}