from django.urls import path, include
from app_disciplines import views


urlpatterns = [
    path('disciplines/', views.dis, name='dis'),
]