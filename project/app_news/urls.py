from django.urls import path
from app_news import views


urlpatterns = [
        path('news/', views.news, name='news'),
]
