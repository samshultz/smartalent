from django.contrib.auth import get_user_model

class EmailAuthBackend(object):
	"""
	Authenticate using an e-mail address.
	"""
	def authenticate(self, request, username=None, password=None):
		try:
			user = get_user_model().objects.filter(email=username).first()
			if user.check_password(password):
				return user
			return None
		except get_user_model().DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return get_user_model().objects.get(pk=user_id)
		except get_user_model().DoesNotExist:
			return None