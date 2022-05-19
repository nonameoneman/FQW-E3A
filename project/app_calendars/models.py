from datetime import datetime
from django.db import models
from django.forms import CharField

# Create your models here.

class Ac_years(models.Model):
    name = models.CharField(("Учебный год"), max_length=50, null=True)
    year_s = models.DateField(("Начало года"), auto_now=False, auto_now_add=False, null=True)
    year_e = models.DateField(("Конец года"), auto_now=False, auto_now_add=False, null=True)
    m1_s = models.DateField(("Начало M1"), auto_now=False, auto_now_add=False, null=True)
    m1_e = models.DateField(("Конец M1"), auto_now=False, auto_now_add=False, null=True)
    m2_s = models.DateField(("Начало M2"), auto_now=False, auto_now_add=False, null=True)
    m2_e = models.DateField(("Конец M2"), auto_now=False, auto_now_add=False, null=True)
    fx1_s = models.DateField(("Начало FX (зим.)"), auto_now=False, auto_now_add=False, null=True)
    fx1_e = models.DateField(("Конец FX (зим.)"), auto_now=False, auto_now_add=False, null=True)
    i1_s = models.DateField(("Начало I (зим.)"), auto_now=False, auto_now_add=False, null=True)
    i1_e = models.DateField(("Конец I (зим.)"), auto_now=False, auto_now_add=False, null=True)
    m3_s = models.DateField(("Начало M3"), auto_now=False, auto_now_add=False, null=True)
    m3_e = models.DateField(("Конец M3"), auto_now=False, auto_now_add=False, null=True)
    m4_s = models.DateField(("Начало M4"), auto_now=False, auto_now_add=False, null=True)
    m4_e = models.DateField(("Конец M4"), auto_now=False, auto_now_add=False, null=True)
    fx2_s = models.DateField(("Начало FX (лет.)"), auto_now=False, auto_now_add=False, null=True)
    fx2_e = models.DateField(("Конец FX (лет.)"), auto_now=False, auto_now_add=False, null=True)
    i2_s = models.DateField(("Начало I (лет.)"), auto_now=False, auto_now_add=False, null=True)
    i2_e = models.DateField(("Конец I (лет.)"), auto_now=False, auto_now_add=False, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Учебный год'
        verbose_name_plural = 'Учебные годы'
        ordering = ['year_s', 'year_e']    