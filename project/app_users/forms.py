from django import forms
from django.contrib.auth.forms import UserChangeForm

from app_users.models import User

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number')