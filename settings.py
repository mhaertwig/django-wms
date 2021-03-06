"""
Settings for django-tiles tests and sphinx build
"""

import os
SECRET_KEY = 'testkey'

INSTALLED_APPS = (
    'wms',
)

DATABASES = {
    'default': {
        'ENGINE':   'django.contrib.gis.db.backends.postgis',
        'USER':     os.environ.get('DB_USER', 'postgres'),
        'HOST':     os.environ.get('DB_HOST', 'localhost'),
        'NAME':     os.environ.get('DB_NAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'PORT':     os.environ.get('DB_PORT', '5432')
    }
}

DEBUG = True

WMS_RASTER_PYRAMID_SRID = '3857'
