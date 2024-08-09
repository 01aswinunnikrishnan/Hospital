from django.db import models
from django.utils import  timezone

# Create your models here.

class userreg(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    Password = models.CharField(max_length=25)
    profilepic=models.ImageField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
class doctorreg(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    Password = models.CharField(max_length=25)
    profilepic=models.ImageField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Blogs(models.Model):
    author = models.ForeignKey(doctorreg,on_delete=models.CASCADE)
    title=models.CharField(max_length=25)
    image=models.FileField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    summary=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    is_draft=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Appointment(models.Model):
    patient = models.ForeignKey(userreg, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=25)
    date = models.DateField()
    start_time = models.TimeField()
    doctor = models.ForeignKey(doctorreg,on_delete=models.CASCADE)
    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.start_time}"

class DoctorOAuthToken(models.Model):
    doctor = models.OneToOneField('doctorreg', on_delete=models.CASCADE)
    access_token = models.TextField()
    refresh_token = models.TextField()
    token_expiry = models.DateTimeField()

