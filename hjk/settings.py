import sys
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# 设置多个应用路径
sys.path.insert(0, os.path.join(BASE_DIR, 'study_resource'))
sys.path.insert(0, os.path.join(BASE_DIR, 'personal_project'))

# 多级templates不警告
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-htlulk@xx8b2cth#q75=icnu1u02r%i22p#h6)vpcoa-24**3_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'study_resource.home',
    'study_resource.users',

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

ROOT_URLCONF = 'hjk.urls'

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

WSGI_APPLICATION = 'hjk.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {},
    'study': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '192.168.1.132',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'blog'  # 数据库名字
    },
    'project': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '192.168.1.132',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'alloygame'  # 数据库名字
    },
}

DATABASE_ROUTERS = [
    # 'path.to.PrimaryReplicaRouter',
    'hjk.database_router.Study', 'hjk.database_router.Project'
]

DATABASE_APPS_MAPPING = {
    # example:
    # 'app_name':'database_name',
    # 'admin': 'defualt',
    'study_resource': 'blog',
    'personal': 'alloygame',
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 设置redis
CACHES = {
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {  # session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# 自定义User模型代替系统的User
AUTH_USER_MODEL = 'users.User'

# 设置未登录用户，必须登录的跳转连接
LOGIN_URL = '/study/login/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# 图片的统一路由
MEDIA_URL = '/media/'
#
# # 设置Django的文件存储类
# DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FDFSStorage'
#
# # 设置fdfs使用的client.conf文件路径
# FDFS_CLIENT_CONF = './personal_project/utils/fdfs/client.conf'
#
# # 设置fdfs存储服务器上nginx的IP和端口号
# FDFS_URL = 'http://192.168.1.132:8888/'
#
# # 全文检索框架的配置
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         # 使用whoosh引擎
#         # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#         'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
#         # 索引文件路径
#         'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
#     }
# }
#
# # 当添加、修改、删除数据时，自动生成索引
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
