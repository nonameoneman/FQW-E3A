from django.urls import path, include
from app_assistant import views


urlpatterns = [
    path('assistant/', views.my_redirect, name='my_redirect'),
]