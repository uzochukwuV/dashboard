from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
    
class new_members(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password_1 = models.IntegerField
    password_2 = models.IntegerField
    
class login(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password_1 = models.IntegerField