from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import CandidateProfile, OrganizationProfile, Job


class LoginForm(AuthenticationForm):
	...


class UserRegistrationForm(forms.ModelForm):

	USER_CHOICES = (
		('candidate', 'Candidate'),
		("employer", 'Employer')
	)

	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
	organization_name = forms.CharField(label="Organization_name", required=False)
	user_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.HiddenInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']


class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class CandidateProfileEditForm(forms.ModelForm):
	class Meta:
		model = CandidateProfile
		exclude = "user",


class OrganizationProfileEditForm(forms.ModelForm):
	class Meta:
		model = OrganizationProfile
		exclude = "user",


class JobCreationForm(forms.ModelForm):
	class Meta:
		model = Job
		exclude = "posted_by", "applied_for_by"