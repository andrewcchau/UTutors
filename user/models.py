from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     bio = models.CharField(max_length=200, default='i am a student')
#
# class Tutor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     price = models.DecimalField
#     rating = models.DecimalField
#     bio = models.CharField(max_length=200, default='i am a tutor')
#     num_students = models.IntegerField
#     students = models.ManyToManyField(Student)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, default='hi')
    TYPE = (
        ('Student', 'Student'),
        ('Tutor', 'Tutor')
    )
    type =  models.CharField(max_length=7, choices=TYPE, default='Student')
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2, blank=True, null=True)


class Course(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(Profile, related_name='students', blank=True)
    tutors = models.ManyToManyField(Profile, related_name='tutors', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # print('a;sdklfjasdklf;jasd;klfj')
    print(instance)
    instance.profile.save()
