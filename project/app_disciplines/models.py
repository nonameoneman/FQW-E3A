from tabnanny import verbose
from xmlrpc.client import boolean
from django.db import models
from django.forms import CharField
from django.urls import reverse


# Create your models here.

class Form_controls(models.Model):
    name = models.CharField(("Название"), max_length=50, null=True)
    short_name = models.CharField(("Короткое название"), max_length=50, null=True)
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'Форму контроля'
        verbose_name_plural = '3. Формы контроля'
        ordering = ['-name',]    
        
class Faculty(models.Model):
    name = models.CharField(("Название"), max_length=150)
    short_name = models.CharField(("Короткое название"), max_length=50)
    cipher = models.IntegerField(("Шифр факультета"), null=True)
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = '1. Факультеты'
        ordering = ['-name',]

class Department(models.Model):
    name = models.CharField(("Название"), max_length=150)
    short_name = models.CharField(("Короткое название"), max_length=50)
    сipher = models.IntegerField(("Шифр отделения"), null=True)
    faculty = models.ForeignKey("app_disciplines.Faculty", verbose_name=("Факультет"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = ("Кафедру")
        verbose_name_plural = ("2. Кафедры")

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Disciplines(models.Model):
    name = models.CharField(("Название"), max_length=150)
    short_name = models.CharField(("Короткое название"), max_length=75)
    credits = models.IntegerField(("Количество кредитов"), null=True)
    hours = models.IntegerField(("Количество часов"), null=True)
    department = models.ForeignKey("app_disciplines.Department", verbose_name=("Отделение"), on_delete=models.PROTECT, null=True)
    form_control = models.ForeignKey("Form_controls", verbose_name=("Форма контроля"), on_delete=models.PROTECT, null=True)
    teacher = models.ForeignKey("app_users.Teacher", verbose_name=("Преподаватель"), on_delete=models.PROTECT, null=True)
    fh = models.BooleanField(("Первое полугодие"), null=True)
    sh = models.BooleanField(("Второе полугодие"), null=True)
    xtr = models.BooleanField(("Дополнительно"), null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def teacher_name(self):
        return self.teacher.name
    teacher_name.fget.short_description = 'ФИО Преподавателя'
    
    class Meta:
        verbose_name = 'Дисциплину'
        verbose_name_plural = '4. Дисциплины'
        ordering = ['name', ] 

class Discipline_reg(models.Model):
    discipline = models.ForeignKey("Disciplines", verbose_name=("Название дисциплины"), related_name='groups', on_delete=models.PROTECT)
    student = models.ForeignKey("app_users.Student", verbose_name=("Шифр студента"), related_name='student', on_delete=models.PROTECT)  
    date_of_reg = models.DateField(("Дата регистрации"), auto_now=False, auto_now_add=True)
    conf = models.BooleanField(("Подтверждаю"), default=False)
    abon = models.BooleanField(("Отказываю"), default=False)
    send = models.BooleanField(("Отправить советнику"), default=False)
    academ_c = models.BooleanField(("Подтверждение советника"), default=False)
    academ_a = models.BooleanField(("Отказ советника"), default=False)
    
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
        verbose_name_plural = '5. Регистрации на предметы'
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