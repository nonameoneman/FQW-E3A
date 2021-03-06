from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from app_users.models import *

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    
    list_display = ('id', 'full_name', 'phone_number', 'email', 'is_advisor', 'is_teacher', 'is_active', 'is_staff')
    list_display_links = ('id', 'full_name', 'phone_number', 'email')
    search_fields = ('full_name', 'phone_number', 'email')
    list_editable = ('is_active',)
    list_filter = ('is_advisor', 'is_superuser', 'is_teacher')
    

    fieldsets = (
        ('Редактор', {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number', 'email', 'is_active',)
                }),
            )
    add_fieldsets = (
        ('Создание', {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'phone_number', 'password1', 'password2', 'is_active', 'is_advisor', 'is_teacher'),
        }),
    )

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    model = Advisor
    
    list_display = ('id', 'name', 'email', 'phone', 'user_id')
    list_display_links = ('id', 'name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    
    list_display = ('id', 'name', 'email', 'phone', 'position', 'user_id')
    list_display_links = ('id', 'name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    
admin.site.unregister(Group)

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    model = Groups
    
    list_display = ('id', 'name', 'cours', 'form_of_e', 'credit_price', 'advisor', 'department')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('department', 'cours', 'form_of_e', 'advisor')
    
#@admin.register(Form_e)
#class FormEAdmin(admin.ModelAdmin):
#    model = Groups
#    
#    list_display = ('id', 'name')
#    list_display_links = ('id', 'name')
#    search_fields = ('id', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    
    list_display = ('id', 'cipher', 'name', 'groups', 'course', 'form_of_e', 'advisor')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('groups', )