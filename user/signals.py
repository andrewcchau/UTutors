from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
# from user.models import Course, Tutor, Student

# @receiver(m2m_changed)
# def my_callback(sender, **kwargs):
#     print("class open!")
#     # let all students subscribed know that a class is open

