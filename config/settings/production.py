from .base import *

env_path = 'envs/.env'
load_dotenv(dotenv_path=env_path, verbose=True)
env = os.getenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = False

THIRD_PARTY_APPS += [

]

# Database ------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('SQL_DATABASE'),
        'USER': env('SQL_USER'),
        'PASSWORD': env('SQL_PASSWORD'),
        'HOST': env('SQL_HOST'),
        'PORT': env('SQL_PORT'),
    }
}
