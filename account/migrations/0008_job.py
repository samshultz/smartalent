# Generated by Django 3.1.3 on 2020-11-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20201115_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('job_type', models.CharField(blank=True, choices=[('freelance', 'Freelance'), ('fulltime', 'Full time'), ('in-house', 'In-house'), ('parttime', 'Part time'), ('remote', 'Remote'), ('temporary', 'Temporary')], max_length=12)),
                ('required_skills', models.CharField(blank=True, max_length=300)),
                ('salary_frequency', models.CharField(blank=True, choices=[('monthly', 'Monthly'), ('annually', 'Annually'), ('negotiable', 'Negotiable')], max_length=10)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('experience', models.CharField(blank=True, choices=[('fresh', 'Fresh'), (1, 'less than 1 year'), (2, '2 years'), (3, '3 years'), (4, '4 years'), (5, '5 years'), (6, '6 years'), (7, '7 years'), (8, '8 years +')], max_length=23)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('female or male', 'Female or Male')], max_length=20)),
                ('qualifications', models.CharField(blank=True, choices=[('no formal qualification', 'No Formal Qualification'), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('bsc', "Bachelor's Degree"), ('msc', "Master's Degree")], max_length=23)),
            ],
        ),
    ]
