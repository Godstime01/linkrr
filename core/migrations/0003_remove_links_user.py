# Generated by Django 5.0 on 2023-12-26 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_usermodel_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='user',
        ),
    ]