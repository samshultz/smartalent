from django.core.exceptions import PermissionDenied
from .models import Job

def user_is_employer(function):
	def wrap(request, *args, **kwargs):
		if request.user.profile:
			return function(request, *args, **kwargs)
		else:
			raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def employer_is_job_author(function):
	def wrap(request, *args, **kwargs):
		job = Job.objects.get(pk=kwargs['job_id'])
		if job.posted_by.company_name == request.user.profile.company_name:
			return function(request, *args, **kwargs)
		else:
			raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap