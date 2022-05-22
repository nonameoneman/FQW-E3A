from django.shortcuts import redirect
from django.urls import path, include, re_path
from app_users import views
from django.contrib import admin
from django.utils.translation import ugettext_lazy 

admin.site.site_title = 'Админпанель E3A'
admin.site.site_header = 'Администрирование E3A'
admin.site.site_title = 'Сайт администрации E3A'

urlpatterns = [
        path('empty_login/', views.login, name='login'),
        path('', include('django.contrib.auth.urls')),
        path('', views.empty, name='empty'),
]