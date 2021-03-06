from turtle import title
from xml.etree.ElementInclude import include
from django.urls import path, include
from app_profiles import views



urlpatterns = [
        path('edit_profile/', views.EditProfileView.as_view(), name='profile'),
        path('password/', views.EditPasswordView.as_view(), name='password'),
]