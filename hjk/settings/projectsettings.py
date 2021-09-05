from .settings import *


DEFAULT_CONFIG = {
    'theme': 'silver',
    'width': 600,
    'height': 400,
}

AUTH_USER_MODEL = 'user.User'

# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# smtp服务器地址
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = '25'
# 发送邮件的邮箱
EMAIL_HOST_USER = "hjk1321252@163.com"
# 授权密码
EMAIL_HOST_PASSWORD = 'FZXIQXXOJHZBONGH'
# 收件人看到的发件人
EMAIL_FROM = '合金游戏<hjk1321252@163.com>'

# redis缓存设置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.1.132/9",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 配置session存储方式
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# 未登录跳转到指定的地址
LOGIN_URL = '/user/login/'

# 设置Django的文件存储类
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FDFSStorage'

# 设置fdfs使用的client.conf文件路径
FDFS_CLIENT_CONF = './utils/fdfs/client.conf'

# 设置fdfs存储服务器上nginx的IP和端口号
FDFS_URL = 'http://192.168.1.132:8888/'

# 全文检索框架的配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'