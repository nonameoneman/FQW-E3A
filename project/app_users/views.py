from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from app_assistant import urls

def loginPage(request):
        if request.user.is_active == False:
                return render(request, 'registration/login.html', {'title':'Страница входа'})
        else:
                return render(request, 'my_redirect')
        edif
