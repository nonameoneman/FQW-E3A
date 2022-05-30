from pyexpat import model
from urllib import request
from django import forms
from django.forms import ModelForm
from .models import Discipline_reg
from app_users.models import *

class DisciplineRegFrom(ModelForm):
    
    class Meta:
        initial= {'student': Student.get_student(User)}
        model = Discipline_reg
        fields = ('discipline', 'student')