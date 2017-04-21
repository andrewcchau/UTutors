from django.shortcuts import render
from .models import Student, Tutor, Course
# Create your views here.

# def index(request):
#     list_of_students = Student.objects.all()
#     context = {'list_of_students': list_of_students}
#     return render(request, 'user/homepage.html', context)

def index(request):
    return render(request, 'user/homepage.html', {})

def classes(request):
    list_of_classes = Course.objects.all()
    context = {'list_of_courses': list_of_classes}
    return render(request, 'user/classes.html', context)


# def profile(request):
#     student =