from re import template
from turtle import title
from urllib import request
from venv import create
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app_profiles.forms import CustomChangeForm
from django.views import generic
from app_users.models import UserManager
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

class EditPasswordView(PasswordChangeView):
    form_class: PasswordChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/password_change.html'

class EditProfileView(generic.UpdateView):
    form_class = CustomChangeForm
    success_url = reverse_lazy('my_redirect')
    template_name ='registration/edit_profile.html'
    
    def get_object(self):
        return self.request.user