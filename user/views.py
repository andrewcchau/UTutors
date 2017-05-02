from django.shortcuts import render, redirect
from django.http import Http404
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import UserForm, ProfileForm, MyForm


# Create your views here.


def index(request):
    return render(request, 'user/homepage.html', {})


@login_required
def classes(request):
    list_of_classes = Course.objects.all()
    context = {'list_of_courses': list_of_classes}
    return render(request, 'user/classes.html', context)


@login_required
def class_profile(request, class_num):
    try:
        course = Course.objects.get(pk=class_num)
    except Course.DoesNotExist:
        raise Http404('This is not a class')
    title = course.name
    tutors = course.tutors.all()
    return render(request, 'user/class_profile.html', {
        'name': title,
        'tutors': tutors,
    })


@login_required
@transaction.atomic
def update_profile(request, profile_num):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        # my_form = MyForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            # my_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        # my_form = MyForm(request.POST)
    return render(request, 'user/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        # 'my_form': my_form,
    })
