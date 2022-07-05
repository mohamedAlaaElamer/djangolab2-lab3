from django.db import models

# Create your models here.
class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    username =models.CharField(max_length=20)
    password=models.CharField(max_length=8,null=True)
    email=models.EmailField(max_length=50,null=True)

class student(models.Model):
    id=models.AutoField(primary_key=True)
    #name=models.CharField(max_length=50)