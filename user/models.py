from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200, default='i am a student')

class Tutor(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField
    rating = models.DecimalField
    bio = models.CharField(max_length=200, default='i am a tutor')
    classes = models.CharField(max_length=200)