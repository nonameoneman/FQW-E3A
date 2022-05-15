from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from app_users.models import User, Advisor


def login(request):
        if request.user.is_authenticated == False:
                return render(request, 'registration/login.html', {'title':'Страница входа'})
        elif request.user.is_staff == True:
                return render(request, 'app_users/admin.redirect.html', {'title':'Переход в панель администратора'})
        elif request.user.is_advisor == True:
                return render(request, 'app_assistant/assistant_a.html', {'title':'Ассистент академического советника'})
        else:
                return render(request, 'app_assistant/assistant_s.html', {'title':'Ассистент студента'})
        endif