from .base import *

DEBUG = False

ALLOWED_HOSTS = ['smartalent.pythonanywhere.com', 'www.smartalent.pythonanywhere.com']
ADMINS = (
	('Antonio M', 'email@mydomain.com'),
)

SECRET_KEY = 'c(4pkz=@$#%$%Y^YTG&^Y&*IUHJIKNJKHTRYD%^&^*&y98oyhiyi756on=p#tc-7(yfka&1!+t_a*7f7757$(l&(j@m-(llfzw'

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'smartalent$default',
		'USER': 'smartalent',
		'PASSWORD': 'reductionism',
		'HOST': 'smartalent.mysql.pythonanywhere-services.com'
	}
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True