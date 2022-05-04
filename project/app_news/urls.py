from django.urls import path
from app_news import views


urlpatterns = [
        path('news/a/', views.news_a, name='news_a'),
        path('news/s/', views.news_s, name='news_s'),
]
