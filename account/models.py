from django.db import models
from django.conf import settings


class TechStack(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name 



class CandidateProfile(models.Model):
	
	MALE = 'Male'
	FEMALE = 'Female'

	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female')
	)

	# No Formal Qualification
	NFQ = "no formal qualification"
	CERTIFICATE = 'certificate'
	DIPLOMA = 'diploma'
	BSC = 'bsc'
	MSC = 'msc'

	ACADEMIC_LEVEL_CHOICES = (
		(NFQ, "No Formal Qualification"),
		(CERTIFICATE, "Certificate"),
		(DIPLOMA, "Diploma"),
		(BSC, "Bachelor's Degree"),
		(MSC, "Master's Degree")
	)
	EXPERIENCE_CHOICES = [(str(i), f"{i}-{i+1} years") for i in range(11)]

	MONTHLY = 'Monthly'
	ANNUALLY = 'Annually'
	SALARY_FREQUENCY_CHOICES = (
		(MONTHLY, 'Monthly'),
		(ANNUALLY, 'Annually')
	)

	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE)
	phone_no = models.CharField(max_length=11, blank=True)
	age = models.IntegerField(null=True, blank=True)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
	about_me = models.TextField(blank=True)
	job_title = models.CharField(max_length=50, blank=True)
	salary_amount = models.IntegerField(null=True)
	salary_frequency = models.CharField(max_length=10, choices=SALARY_FREQUENCY_CHOICES, blank=True)
	academic_level = models.CharField(max_length=25, choices=ACADEMIC_LEVEL_CHOICES, blank=True)
	years_of_experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES, blank=True)
	date_of_birth = models.DateField(blank=True, null=True)
	cover_photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

	linkedin_url = models.URLField(blank=True)
	github_url = models.URLField(blank=True)

	stack = models.ManyToManyField(TechStack, related_name="stack", blank=True)
	
	def __str__(self):
		return f'Profile for user {self.user.username}'


class OrganizationProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', 
								on_delete=models.CASCADE)
	company_name = models.CharField(max_length=200, blank=True)
	phone_no = models.CharField(max_length=11, blank=True)
	website = models.URLField(blank=True)
	founded_date = models.DateField(blank=True, null=True),
	description = models.TextField(blank=True)
	cover_photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	
	facebook_url = models.URLField(blank=True)
	twitter_url = models.URLField(blank=True)
	linkedin_url = models.URLField(blank=True)

	def __str__(self):
		return f"Profile for organization {self.company_name}"


class Job(models.Model):
	FREELANCE = "freelance"
	FULLTIME = "fulltime"
	INHOUSE = "in-house"
	PARTTIME = "parttime"
	REMOTE = "remote"
	TEMPORARY = 'temporary'

	MONTHLY = 'monthly'
	ANNUALLY = 'annually'
	NEGOTIABLE = 'negotiable'

	SALARY_FREQUENCY_CHOICES = (
		(MONTHLY, 'Monthly'),
		(ANNUALLY, 'Annually'),
		(NEGOTIABLE, 'Negotiable')
	)

	JOB_TYPE_CHOICES = (
		(FREELANCE, "Freelance"),
		(FULLTIME, 'Full time'),
		(INHOUSE, 'In-house'),
		(PARTTIME, 'Part time'),
		(REMOTE, 'Remote'),
		(TEMPORARY, "Temporary")
	)

	EXPERIENCE_CHOICES = [("fresh", "Fresh"), (1, "less than 1 year")]
	OTHER_EXPERIENCE_CHOICES = [(str(i), f"{i} years") for i in range(2, 8)]
	EXPERIENCE_CHOICES.extend(OTHER_EXPERIENCE_CHOICES)
	EXPERIENCE_CHOICES.extend([("8", "8 years +")])

	MALE = 'male'
	FEMALE = 'female'
	BOTH = 'female or male'

	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(BOTH, "Female or Male")
	)

	posted_by = models.ForeignKey(OrganizationProfile, related_name='posted_jobs', 
								on_delete=models.CASCADE, blank=True)
	applied_for_by = models.ManyToManyField(CandidateProfile, 
											related_name='applied_jobs', 
											blank=True)
	title = models.CharField(max_length=300)
	description = models.TextField()

	# application deadline
	daterange = models.DateField()
	job_type = models.CharField(max_length=12, choices=JOB_TYPE_CHOICES, blank=True)
	required_skills = models.ManyToManyField(TechStack, related_name='jobs', blank=True)
	salary_frequency = models.CharField(max_length=10, choices=SALARY_FREQUENCY_CHOICES, blank=True)
	min_salary = models.DecimalField(decimal_places=0, max_digits=6, blank=True, null=True)
	max_salary = models.DecimalField(decimal_places=0, max_digits=6, blank=True, null=True)

	experience = models.CharField(max_length=23, choices=EXPERIENCE_CHOICES, blank=True)

	gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
	qualifications = models.CharField(max_length=23, choices=CandidateProfile.ACADEMIC_LEVEL_CHOICES, blank=True)

	def __str__(self):
		return f"{self.title} posted by {self.posted_by.company_name}"
