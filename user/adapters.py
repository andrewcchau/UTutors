from allauth.account.adapter import DefaultAccountAdapter
from django import forms
from django.http import HttpResponse
from django.utils.translation import gettext as _

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        email = data['email']
        email = email.partition('@')
        if email[2] == 'utexas.edu':
            print('hello')
        else:
            return HttpResponse('/')
        return user
