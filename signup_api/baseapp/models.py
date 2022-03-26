from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    courseName = models.CharField(max_length=200)
    courseFee = models.FloatField(null=True)
    courseTeacher = models.CharField(max_length=200)