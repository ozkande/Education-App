from django import forms
from . models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class UserForm(UserCreationForm):
    email =forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

