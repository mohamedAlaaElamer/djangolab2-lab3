from django.db import models

class Course(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=200)
     hours=models.IntegerField()

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    nationalnum=models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)