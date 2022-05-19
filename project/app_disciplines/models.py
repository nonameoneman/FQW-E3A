from tabnanny import verbose
from django.db import models
from django.forms import CharField


# Create your models here.

class Form_controls(models.Model):
    name = models.CharField(("Название"), max_length=50, null=True)
    short_name = models.CharField(("Короткое название"), max_length=50, null=True)
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'Форму контроля'
        verbose_name_plural = 'Формы контроля'
        ordering = ['-name',]    

class Disciplines(models.Model):
    name = models.CharField(("Название"), max_length=150)
    short_name = models.CharField(("Короткое название"), max_length=75)
    credits = models.IntegerField(("Количество кредитов"), null=True)
    hours = models.IntegerField(("Количество часов"), null=True)
    form_control = models.ForeignKey("Form_controls", verbose_name=("Форма контроля"), on_delete=models.PROTECT)
    fh = models.BooleanField(("Первое полугодие"), null=True)
    sh = models.BooleanField(("Второе полугодие"), null=True)
    xtr = models.BooleanField(("Дополнительно"), null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Дисциплину'
        verbose_name_plural = 'Дисциплины'
        ordering = ['name', ] 

class Discipline_reg(models.Model):
    discipline = models.ForeignKey("Disciplines", verbose_name=("Название дисциплины"), on_delete=models.PROTECT)
    student = models.ForeignKey("app_users.Student", verbose_name=("Шифр студента"), on_delete=models.PROTECT)  
    date_of_reg = models.DateField(("Дата регистрации"), auto_now=False, auto_now_add=True)
    
    @property
    def student_name(self):
        return self.student.name
    student_name.fget.short_description = 'ФИО Студента'
    
    @property
    def credits(self):
        return self.discipline.credits
    credits.fget.short_description = 'Количество кредитов'
    
    @property
    def group_name(self):
        return self.student.groups
    group_name.fget.short_description = 'Группа'
    
    class Meta:
        verbose_name = 'Регистрацию на предмет'
        verbose_name_plural = 'Регистрации на предметы'
        ordering = ['discipline', 'date_of_reg']
        
class Credits_count(models.Model):
    first_half = models.IntegerField(("Первое полугодие"))
    second_half = models.IntegerField(("Второе полугодие"))
    extra = models.IntegerField(("Дополнительно"))
    total = models.IntegerField(("Всего кредитов"))
    dis_reg = models.ForeignKey("Discipline_reg", verbose_name=("Зарегистрированные предметы"), on_delete=models.PROTECT)
    
    def __str__(self):
        return self.total
    
    @property
    def student(self):
        return self.dis_reg.student
    student.fget.short_description = 'Студент'
    
    class Meta:
        verbose_name = 'Колличество кредитов'
        verbose_name_plural = 'Колличество кредитов'
        ordering = ['dis_reg', ]
    