from django.shortcuts import render
from .models import Student, Tutor
# Create your views here.

# def index(request):
#     list_of_students = Student.objects.all()
#     context = {'list_of_students': list_of_students}
#     return render(request, 'user/homepage.html', context)

def index(request):
    return render(request, 'user/base.html')

# def profile(request):
#     student =