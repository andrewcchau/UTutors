from django.test import TestCase
from decimal import *

# Create your tests here.

from .models import Profile, Course

class ProfileTests(TestCase):
    def test_valid_rating(self):
        rating = Decimal(Profile.rating)
        self.assertIs(rating > 0.0, True)

class CourseTest(TestCase):
    def test_valid_name(self):
        name = Course.name
        self.assertIs(len(name) != 0, True)
