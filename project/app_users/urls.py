from xml.etree.ElementInclude import include
from django.urls import path, include
from app_users import views


urlpatterns = [
        path('login2/', views.loginPage, name='loginPage'),
        path('', include('django.contrib.auth.urls')),
]