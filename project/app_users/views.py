from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from app_users.models import User, Advisor


def login(request):
        if request.user.is_authenticated == False:
                return render(request, 'registration/login.html', {'title':'Страница входа'})
        else:
                return redirect('assistant/')
        endif
        
def empty(request):
        if request.user.is_authenticated == False:
                return redirect('login/')
        else:
                return redirect('assistant/')
        endif