from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200, default='i am a student')

class Tutor(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField
    rating = models.DecimalField
    bio = models.CharField(max_length=200, default='i am a tutor')
    num_students = models.IntegerField
    students = models.ManyToManyField(Student)

class Course(models.Model):
    name = models.CharField(max_length=30)
    subscribed = models.ManyToManyField(Student)
    tutors = models.ManyToManyField(Tutor)
