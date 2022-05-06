from django.shortcuts import render, redirect


def login(request):
    return render(request, 'app_users/login.html', {'title':'Страница входа'})