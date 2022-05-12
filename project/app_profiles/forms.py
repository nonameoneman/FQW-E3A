from dataclasses import fields
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from app_users.models import User

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone_number')
        
