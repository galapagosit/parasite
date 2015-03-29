
from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'parasite',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {
           "init_command": "SET storage_engine=MYISAM",
        }
    }
}
