from os import environ
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
REMEMBER_COOKIE_DURATION = timedelta(days=7)
SQLALCHEMY_TRACK_MODIFICATIONS = False
