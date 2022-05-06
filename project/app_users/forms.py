from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from app_users.models import User

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number')

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number')