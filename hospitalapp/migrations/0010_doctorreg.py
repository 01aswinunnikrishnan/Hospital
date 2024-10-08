# Generated by Django 5.0.6 on 2024-07-31 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0009_remove_userreg_usertype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorreg',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('Password', models.CharField(max_length=25)),
                ('profilepic', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
