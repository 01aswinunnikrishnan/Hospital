# Generated by Django 5.0.6 on 2024-07-30 13:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_users_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='userreg',
        ),
    ]
