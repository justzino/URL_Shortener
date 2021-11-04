from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
env_path = 'envs/.env.dev'
load_dotenv(dotenv_path=env_path, verbose=True)
env = os.getenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS += ['originalll.pythonanywhere.com']


THIRD_PARTY_APPS += [

]

# Database ------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
