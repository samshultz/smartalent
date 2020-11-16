from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm, UserRegistrationForm


urlpatterns = [
	path('login/', auth_views.LoginView.as_view(extra_context={'login_form': LoginForm, 
																'reg_form': UserRegistrationForm}), 
												name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	# change password urls
	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	# reset password urls
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('candidate/register/', views.register, name='register'),
	path('profile/', views.candidate_profile_edit, name='profile_edit'),
	path('organization/profile/', views.organization_profile_edit, name='organization_profile_edit'),
	path('applied_jobs/', views.view_applied_jobs, name='applied_jobs'),
	path('job_alert/', views.view_job_alerts, name='job_alert'),
	path('job/create/', views.post_jobs, name='job_create'),
	path('job/manage/', views.manage_jobs, name='job_manage'),
	path('job/delete/<int:job_id>/', views.delete_job, name='job_delete'),
	path('', views.dashboard, name='dashboard'),
]