from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import UserForm, ProfileForm


# Create your views here.


def index(request):
    return render(request, 'user/homepage.html', {})


@login_required
def classes(request):
    list_of_classes = Course.objects.all()
    context = {'list_of_courses': list_of_classes}
    return render(request, 'user/classes.html', context)


@login_required
@transaction.atomic
def update_profile(request, profile_num):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
    return render(request, 'user/profile.html', {
        'user_form': user_form,
        'profile_form':profile_form
    })
