import os

from .common import *

DEBUG = False

ALLOWED_HOSTS = ['gtamk.herokuapp.com']

SECRET_KEY = os.environ['SECRET_KEY']