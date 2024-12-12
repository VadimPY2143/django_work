from django import forms
from Auth.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

