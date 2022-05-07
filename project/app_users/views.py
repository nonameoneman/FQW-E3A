from turtle import title
from urllib import request
from django.shortcuts import render, redirect


def loginPage(request):
        return render(request, 'registration/login.html', {'title':'Страница входа'})
