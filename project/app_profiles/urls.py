from xml.etree.ElementInclude import include
from django.urls import path, include
from app_profiles import views


urlpatterns = [
        path('profile/', views.profile, name='profile'),
        path('', include('django.contrib.auth.urls')),
]