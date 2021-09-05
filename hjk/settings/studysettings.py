from .settings import *

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
LOGIN_URL = '/login/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../../media/')
# 图片的统一路由
MEDIA_URL = '/media/'