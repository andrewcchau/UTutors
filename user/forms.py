from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import InlineRadios
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from .models import Profile


#
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('type', 'bio', 'price', 'rating')


class MyForm(forms.Form):
    TYPE = (
        ('Student', 'Student'),
        ('Tutor', 'Tutor')
    )
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit', css_class= 'btn-primary'))
    helper.layout = Layout(
        InlineRadios('rating'),
    )
