from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class TaskForm(forms.ModelForm):
# You altered User model
    class Meta:
        model = Tasks
        fields = [
            'user',
            'title'
            ]
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

