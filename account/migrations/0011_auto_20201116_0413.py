# Generated by Django 3.1.3 on 2020-11-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20201116_0356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='required_skills',
        ),
        migrations.AddField(
            model_name='job',
            name='required_skills',
            field=models.ManyToManyField(blank=True, related_name='jobs', to='account.TechStack'),
        ),
    ]
