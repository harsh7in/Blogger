from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class user_reg_form(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=['username','email','password1','password2']