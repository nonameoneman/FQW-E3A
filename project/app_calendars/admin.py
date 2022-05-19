from django.contrib import admin
from .models import Ac_years

# Register your models here.

@admin.register(Ac_years)
class AcYearsAdmin(admin.ModelAdmin):
    model = Ac_years
    
    list_display = ('id','name', 'year_s', 'm1_s', 'm2_s', 'fx1_s', 'i1_s', 'm3_s', 'm4_s', 'fx2_s', 'i2_s')
    search_field = ('name',)
    list_filter = ('name',)
