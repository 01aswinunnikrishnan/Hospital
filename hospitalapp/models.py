from django.db import models

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
    

