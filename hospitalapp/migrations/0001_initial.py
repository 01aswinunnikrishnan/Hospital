# Generated by Django 5.0.6 on 2024-07-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=25, null=True, unique=True)),
                ('Password', models.CharField(max_length=25, null=True)),
                ('usertype', models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], max_length=20)),
                ('profilepic', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
