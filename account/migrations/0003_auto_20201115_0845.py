# Generated by Django 3.1.3 on 2020-11-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201115_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
