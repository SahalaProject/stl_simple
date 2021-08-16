"""
Django settings for STL project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import time

str_day = time.strftime("%Y-%m-%d_%H-%M-%S")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOADFILES_DIR = BASE_DIR + r"/uploadFiles/"  # 文件上传路径
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e$od9f28jce8q47u3raik$(e%$@lff6r89ux+=f!e1a$e42+#7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Token Settings
INVALID_TIME = 60 * 60 * 6

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stlapp.apps.StlappConfig',
    'stluser',
    'rest_framework',
    'corsheaders',
]

# STATIC_PATH = r"/opt/AutoPlatform/FilePath/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'STL.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'STL.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# 服务器
# DBHOST = '192.168.87.81'
# DBNAME = 'testdb3'
# DBUSER = 'testdb3'
# DBPASSWORD = '123456'

# 玉斌本地
DBHOST = '127.0.0.1'
DBNAME = 'stl_db'
DBUSER = 'root'
DBPASSWORD = 'li123456'

# 192.168.126.104 线上
# DBHOST = '192.168.126.104'
# DBNAME = 'stl'
# DBUSER = 'w'
# DBPASSWORD = 'zhuanxiangzu'

# 柳伟本地
# DBHOST = '192.168.98.169'
# DBNAME = 'testdb'
# DBUSER = 'root'
# DBPASSWORD = '123456'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DBNAME,
        'USER': DBUSER,
        'PASSWORD': DBPASSWORD,
        'HOST': DBHOST,
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},  # 存储数据库的编码格式问题。
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# rest_framework config

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['STL.auth.Authenticator'],
    'UNAUTHENTICATED_USER': None,
    'UNAUTHENTICATED_TOKEN': None,
    'DEFAULT_PERMISSION_CLASSES': ['STL.stlPermissions.VisitPermission'],

    # json form 渲染
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser',
                               'rest_framework.parsers.FormParser',
                               'rest_framework.parsers.MultiPartParser',
                               'rest_framework.parsers.FileUploadParser',
                               ],
    'DEFAULT_THROTTLE_CLASSES': ['STL.stlThrottling.AnonThrottle', 'STL.stlThrottling.UserThrottle'],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/m',
        'user': '180/m',
    },
    'DEFAULT_PAGINATION_CLASS': 'STL.pagination.MyPageNumberPagination',
}

# DRF扩展缓存时间
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间 单位 秒
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 10,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

EMAIL_SEND_USERNAME = 'Arile_LLL@163.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需开通smtp服务
EMAIL_SEND_PASSWORD = 'liuwei115@'  # 邮箱密码
SERVER_URL = "http://192.168.87.81:8000"  # 服务器地址
WEB_HOOK_TOKEN = "https://oapi.dingtalk.com/robot/send?access_token=ca6456f1b1520cb45419ec7e92b1354641b7fd7af294663d0402dc240ed7aeb5"  # 专项组的webhook


LOGS_ROOT = os.path.join(BASE_DIR, 'logs')
LOGS_ROOT if os.path.exists(LOGS_ROOT) else os.makedirs(LOGS_ROOT)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] - %(message)s'}
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/run.log'),
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/run.log'),
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'FasterRunner.app': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'FasterRunner': {
            'handlers': ['scprits_handler', 'console'],
            'level': 'INFO',
            'propagate': True
        }
    }
}


TIME_TASK_TYPE = 'apscheduler'  # 根据启动的 apscheduler  /  celery 来切换兼容 定时任务手动执行时方式

SUMMARY_SIZE = 6971520  # 超过20M的报告以文件保存 20971520
REPORT_ROOT = os.path.join(BASE_DIR, 'media', 'report')
REPORT_ROOT if os.path.exists(REPORT_ROOT) else os.makedirs(REPORT_ROOT)
