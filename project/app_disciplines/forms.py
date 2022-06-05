from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import Discipline_reg
from app_users.models import *

        

class DisciplineRegFrom(ModelForm):
    
    class Meta:
        model = Discipline_reg
        fields = ('student', 'discipline')
        success_url = reverse_lazy('dis')