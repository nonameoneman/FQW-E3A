import os # ипортирую os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-jop*)(k5yx&0us^m5b$#8$fn9j#vw9r3(ss%x=x$&-y)tybe_f'


DEBUG = True


ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa', # расширение PWA
    'crispy_forms', # расширение для правильной работы форм и Bootstrap
    "crispy_bootstrap5",
    'app_users.apps.AppUsersConfig', # переопределенное приложение пользователя   
    'app_profiles.apps.AppProfilesConfig', # приложение профиля
    'app_assistant.apps.AppAssistantConfig', # приложение ассистента
    'app_news.apps.AppNewsConfig', # приложение новостей
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # определяю что подключен PostgreSQL через расширение psycopg2
        'NAME': 'project_db', # название базы данных
        'USER' : 'owner_db', # владелец базы данных
        'PASSWORD' : 'um5V5ZFvJQ1FvgZEsqC4QaK5PF3HQeq3', # пароль владельца базы данных
        'HOST' : '127.0.0.1', # хост базы данных
        'PORT' : '5432', # порт базы данных
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'app_users.User' # переопределяю модель пользователя

LOGIN_REDIRECT_URL = 'my_redirect'

LOGOUT_REDIRECT_URL = '/login'

LANGUAGE_CODE = 'ru' # определяю язык проекта

TIME_ZONE = 'UTC' # определяю время проекта

USE_I18N = True

USE_L10N = True

USE_TZ = True


# определяю каталог статичных файлов
STATIC_URL = 'static/'  

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static'),
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# настраиваю PWA расширение
PWA_APP_NAME = 'E3A' 
PWA_APP_DESCRIPTION = "Электронный Ассистент" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#ffffff' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'portrait' 
PWA_APP_START_URL = '/login/' 
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [ { 'src': '/static/android-chrome-512x512.png', 'sizes': '512x512' } ] 
PWA_APP_ICONS_APPLE = [ { 'src': '/static/apple-touch-icon.png', 'sizes': '180x180' } ] 
PWA_APP_SPLASH_SCREEN = [ { 'src': '/static/splash-640x1136.png', 'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)' } ] 
PWA_APP_DIR = 'ltr' 
PWA_APP_LANG = 'ru'
PWA_APP_DEBUG_MODE = True
PWA_SERVICE_WORKER_PATH = 'static/sw.js'

# определение типа форм 
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" 
CRISPY_TEMPLATE_PACK = "bootstrap5"