from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(News)
class CreditsCountAdmin(admin.ModelAdmin):
    model = News
    
    list_display = ('title', 'text', 'advisor', 'date_of_pub',)
    search_field = ('title', 'advisor',)
    