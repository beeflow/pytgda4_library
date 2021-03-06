from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
