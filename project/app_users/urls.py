from django.shortcuts import redirect
from django.urls import path, include
from app_users import views


urlpatterns = [
        path('', views.login, name='login'),
        path('', include('django.contrib.auth.urls')),
]