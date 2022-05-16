from msilib.schema import Class
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_users.models import User, Advisor, Groups, Form_e

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    
    list_display = ('id', 'full_name', 'phone_number', 'email', 'is_advisor', 'is_active', 'is_staff')
    list_display_links = ('id', 'full_name', 'phone_number', 'email')
    search_fields = ('full_name', 'phone_number', 'email')
    list_editable = ('is_active',)
    list_filter = ('is_advisor', 'is_superuser')
    

    fieldsets = (
        ('Редактор', {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number', 'email', 'is_active',)
                }),
            )
    add_fieldsets = (
        ('Создание', {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'phone_number', 'password1', 'password2', 'is_active', 'is_advisor',),
        }),
    )

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    model = Advisor
    
    list_display = ('id', 'name', 'email', 'phone', 'position', 'user_id')
    list_display_links = ('id', 'name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    model = Groups
    
    list_display = ('id', 'name', 'cours', 'advisor')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
@admin.register(Form_e)
class FormEAdmin(admin.ModelAdmin):
    model = Groups
    
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
