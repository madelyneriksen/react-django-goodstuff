"""Settings for production."""


from .base import *


DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = []
ADMINS = []
