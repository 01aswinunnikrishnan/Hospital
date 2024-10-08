# Generated by Django 5.0.6 on 2024-08-03 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0011_remove_doctorreg_user_remove_userreg_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('image', models.FileField(upload_to='')),
                ('summary', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.doctorreg')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.category')),
            ],
        ),
    ]
