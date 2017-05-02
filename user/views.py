from django.shortcuts import render, redirect
from django.http import Http404
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, Profile
from .forms import UserForm, ProfileForm
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return render(request, 'user/homepage.html', {})


@login_required
def subscribe(request, class_num):
    print(request.user)
    print(class_num)
    # print(profile)
    try:
        course = Course.objects.get(pk=class_num)
    except Course.DoesNotExist:
        raise Http404('Something went wrong')
    mypk = request.user.profile.pk
    try:
        is_subscribed = course.tutors.get(pk=mypk)
    except Profile.DoesNotExist:
        is_subscribed = None
        course.tutors.add(request.user.profile)
    if is_subscribed != None:
        course.tutors.remove(request.user.profile)
    return redirect(class_profile, class_num)


@login_required
def request_tutor(request, class_num):
    try:
        course = Course.objects.get(pk=class_num)
    except Course.DoesNotExist:
        raise Http404('Something went wrong')
    body = 'Hi, a student in your class ' + course.name + ' is requesting a tutor! contact them!'
    for x in course.tutors.all():
        send_mail('Student Request', body, 'admin@UTutors.com', [x.user.email], fail_silently=False)
    return redirect(class_profile, class_num)


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
        'class_num': class_num
    })


@login_required
def profile(request, profile_num):
    try:
        profile = Profile.objects.get(pk=profile_num)
    except Profile.DoesNotExist:
        raise Http404('This student does not exist')
    name = profile.user.get_full_name
    print(name)
    print('hi')
    bio = profile.bio
    type = profile.get_type_display()
    if type == 'Tutor':
        price = profile.price
    else:
        price = 0
    return render(request, 'user/profile.html', {
        'name': name,
        'bio': bio,
        'type': type,
        'price': price,
        'profile': profile,
    })


@login_required
@transaction.atomic
def update_profile(request, profile_num):
    try:
        profile = Profile.objects.get(pk=profile_num)
    except Profile.DoesNotExist:
        raise Http404('This student does not exist')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=profile.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        # my_form = MyForm(request.POST)
        user_fields = user_form.data
        user_form = UserForm(user_fields, instance=profile.user)
        # print(user_fields)
        # print(user_form)
        # print(user_form.is_bound)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # my_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile', profile_num)
        else:
            print(user_form.errors)
            messages.error(request, _('Please correct the error'))
    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        # my_form = MyForm(request.POST)
    return render(request, 'user/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        # 'my_form': my_form,
    })
