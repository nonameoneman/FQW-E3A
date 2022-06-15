from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import *
from app_users.models import *

class NewsForm(ModelForm):
    
    class Meta:
        model = News
        fields = ('title', 'text', 'advisor')
        success_url = reverse_lazy('news')