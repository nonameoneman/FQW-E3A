from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_users.models import User
from app_users.forms import CustomCreationForm, CustomChangeForm

admin.site.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ['full_name', 'phone_number', 'email', 'user_type', 'is_active', 'is_staff']

    add_fields = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'full_name',
                    'email',
                    'phone_number',
                    'user_type',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields', 
            {
                'fields': (
                    'full_name',
                    'email',
                    'phone_number',
                ),
            }
        ),
    )