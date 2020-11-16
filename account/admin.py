from django.contrib import admin
from .models import CandidateProfile, OrganizationProfile, TechStack,Job


admin.site.register(CandidateProfile)
admin.site.register(OrganizationProfile)
admin.site.register(TechStack)
admin.site.register(Job)