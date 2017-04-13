from django import forms

class SignUpForm(forms.Form):
    your_name = forms.CharField(label="your_name", max_length=34)