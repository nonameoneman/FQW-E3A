from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pwa.urls")),
    path('', include("app_users.urls")),
    path('', include("app_profiles.urls")),
    path('', include("app_assistant.urls")),
    path('', include("app_news.urls")),
]