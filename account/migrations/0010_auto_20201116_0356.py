# Generated by Django 3.1.3 on 2020-11-16 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20201116_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='deadline',
            new_name='daterange',
        ),
    ]