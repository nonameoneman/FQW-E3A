from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import *

class NewsForm(ModelForm):
    
    class Meta:
        model = news
        fields = ('advisor', 'title', 'text')
        success_url = reverse_lazy('news')