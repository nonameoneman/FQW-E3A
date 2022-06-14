from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(news)
class CreditsCountAdmin(admin.ModelAdmin):
    model = news
    
    list_display = ('title', 'text', 'advisor', 'date_of_pub',)
    search_field = ('title', 'advisor',)
    