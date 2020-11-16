from .base import *

DEBUG = True

SECRET_KEY = 'c(4pkz=on=p#tc-7(yfka&1!+t_a*7f7757$(l&(j@m-(llfzw'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}