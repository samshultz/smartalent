from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import (UserRegistrationForm,
					LoginForm, UserEditForm,
					CandidateProfileEditForm,
					OrganizationProfileEditForm,
					JobCreationForm)
from .models import OrganizationProfile, CandidateProfile, Job
from .decorators import user_is_employer, employer_is_job_author


def index(request):
	return render(request, "account/index.html")


@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)

		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			user_type = user_form.cleaned_data.get('user_type')
			print(user_type)

			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			messages.success(request, 'Regiistration Successful, Login')

			if user_type == "candidate":
				CandidateProfile.objects.create(user=new_user)
			else:
				OrganizationProfile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user': new_user})
		else:
		    messages.error(request,  'Correct the errors below')



	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form, 'login_form': LoginForm()})


@login_required
def candidate_profile_edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = CandidateProfileEditForm(instance=request.user.user_profile,
												data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save(commit=False)
			profile_form.user = request.user
			profile_form.save()
			messages.success(request, 'Profile Updated Successfully')
		else:
			messages.error(request, 'Error Updating Profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = CandidateProfileEditForm(instance=request.user.user_profile)
	return render(request, 'account/profile.html', {'user_form': user_form,
												'profile_form': profile_form})


@login_required
def organization_profile_edit(request):
	if request.method == "POST":
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = OrganizationProfileEditForm(instance=request.user.profile,
													data=request.POST,
													files=request.FILES
													)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save(commit=False)
			profile_form.user = request.user
			profile_form.save()
			messages.success(request, 'Profile Updated Successfully')
		else:
			messages.error(request, 'Error Updating Profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = OrganizationProfileEditForm(instance=request.user.profile)

	return render(request, 'account/employer_profile.html', {'user_form': user_form,
												'profile_form': profile_form})


@login_required
@user_is_employer
def post_jobs(request):
	if request.method == "POST":
		job_form = JobCreationForm(data=request.POST)

		if job_form.is_valid():
			job = job_form.save(commit=False)
			job.posted_by = request.user.profile
			job.save()
			messages.success(request, 'Job Created Successfully')
		else:
			print(job_form.errors)
			messages.error(request, 'Error Creating Job')
	else:
		job_form = JobCreationForm()

	return render(request, "account/job_create.html", {"job_form": job_form})

@login_required
@user_is_employer
def manage_jobs(request):
	jobs = Job.objects.filter(posted_by__id=request.user.profile.id)
	return render(request, "account/job_manage.html", {"jobs": jobs})


@login_required
@user_is_employer
@employer_is_job_author
def delete_job(request, job_id):
	if request.method == "POST":

		job = get_object_or_404(Job, id=job_id)
		job.delete()
		messages.success(request, "Job Deleted Successfully")
	return redirect(reverse("job_manage"))

@login_required
def view_applied_jobs(request):
	return render(request, 'account/applied_jobs.html')

@login_required
def view_job_alerts(request):
	return render(request, 'account/job_alerts.html')