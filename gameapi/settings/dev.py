from .common import *

from .common import *

DEBUG = True

INTERNAL_IPS = ["127.0.0.1"] # NOTE: djanog_debug_toolbar 용 설정 추가

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR,  'media')