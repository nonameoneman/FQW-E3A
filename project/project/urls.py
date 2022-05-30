from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('', include("pwa.urls")),
    path('', include("app_users.urls")),
    path('', include("app_profiles.urls")),
    path('', include("app_assistant.urls")),
    path('', include("app_news.urls")),
    path('', include("app_disciplines.urls")),
]