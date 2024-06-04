# pylint: disable=missing-function-docstring

import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# Following is for S3 implementation
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE allows collect static automatically put static files in S3.
# May only use when doing initial load and if I update django (to get their css and js changes)
# plan to no longer collect static for my own static files
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
MY_ENV_VAR = os.getenv('MY_ENV_VAR')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'lizschley-static'
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = 'dirl4bhsg8ywj.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
# Trouble-shooting
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = 'us-east-1'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True