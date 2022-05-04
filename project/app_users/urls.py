from django.urls import path
from app_users import views


urlpatterns = [
        path('', views.login, name='login'),
]