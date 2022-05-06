from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_users.models import User
from app_users.forms import CustomCreationForm, CustomChangeForm

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    
    list_display = ('full_name', 'phone_number', 'email', 'is_advisor', 'is_active', 'is_staff')
    list_display_links = ('full_name', 'phone_number', 'email')
    search_fields = ('full_name', 'phone_number', 'email')

    fieldsets = (
        ('Редактирование', {
            'classes': ('wide',),
            'fields': (
                'full_name',
                'phone_number',
                'email',
                'is_active',)
                }),
            )
    add_fieldsets = (
        ('Добавление', {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'phone_number', 'password1', 'password2', 'is_active', 'is_advisor'),
        }),
    )