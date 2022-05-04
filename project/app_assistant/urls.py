from django.urls import path
from app_assistant import views

urlpatterns = [
    path('assistant/a/', views.assistant_a, name='assistant_a'),
    path('assistant/s/', views.assistant_s, name='assistant_s')
]