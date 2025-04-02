# config/settings.py

import os

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-dev-key')
    SESSION_TIMEOUT = 300  # 5 minutes in seconds
