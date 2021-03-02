from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']
