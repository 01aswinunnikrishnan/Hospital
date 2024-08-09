# Generated by Django 5.0.6 on 2024-08-08 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0015_alter_blogs_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.doctorreg')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.userreg')),
            ],
        ),
    ]
