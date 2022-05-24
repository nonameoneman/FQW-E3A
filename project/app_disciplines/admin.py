from django.contrib import admin

from .models import Form_controls, Disciplines, Discipline_reg, Credits_count

# Register your models here.

@admin.register(Form_controls)
class FormControlsAdmin(admin.ModelAdmin):
    model = Form_controls
    
    list_display = ('name', 'short_name',)

@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    model = Disciplines
    
    list_display = ('name', 'short_name', 'credits', 'hours', 'form_control', 'teacher', 'fh', 'sh', 'xtr')
    search_field = ('name', 'short_name')
    list_filter = ('credits', 'hours', 'form_control')
    list_editable = ('teacher', 'fh', 'sh', 'xtr')
    
@admin.register(Discipline_reg)
class DisciplineRegAdmin(admin.ModelAdmin):
    model = Discipline_reg
    
    list_display = ('discipline', 'credits', 'student_name', 'group_name', 'student', 'date_of_reg')
    search_fields = ('discipline', 'student', 'date_of_reg')
    
@admin.register(Credits_count)
class CreditsCountAdmin(admin.ModelAdmin):
    model = Credits_count
    
    list_display = ('student', 'first_half', 'second_half', 'extra', 'total', 'dis_reg')
    search_field = ('dis_reg',)