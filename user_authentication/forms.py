from django.db import models
from django import forms
from django.contrib.auth.models import User
from user_authentication.models import UserProfile

# Create your models here.

class Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.models):
    class Meta():
        model = UserProfile
        fields = ('portfolio')