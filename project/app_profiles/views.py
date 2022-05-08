from turtle import title
from urllib import request
from django.shortcuts import render, redirect


def profile(request):
        if request.user.is_advisor == True:
                return render(request, 'app_profiles/profile_a.html', {'title':'Мой профиль'})
        else:
                return render(request, 'app_profiles/profile_s.html', {'title':'Мой профиль'})
        edif
