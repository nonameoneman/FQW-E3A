from audioop import reverse
from turtle import position
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, phone_number, full_name, password, **extra_fields):
        if not email:
            raise ValueError('Должен быть введен Email')
        if not phone_number:
            raise ValueError('Должен быть введен номер телефона')
        if not full_name:
            raise ValueError('Должны быть введены ФИО')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, phone_number, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone_number, full_name, password, **extra_fields)

    def create_superuser(self, email, phone_number, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь значения is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь значения is_superuser=True.')
        return self._create_user(email, phone_number, full_name, password, **extra_fields)

from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Почта'), max_length=125, unique=True)
    phone_number = models.CharField(_('Номер телефона'), max_length=13, unique=True)
    full_name = models.CharField(_('ФИО'), max_length=125)
#   profile_photo = models.ImageField(_('Фото профиля'), upload_to='avatars/', null=True, blank=True)
    is_advisor = models.BooleanField(_('Cоветник'), default=False)
    is_teacher = models.BooleanField(_('Преподаватель'), default=False)
    is_active = models.BooleanField(_('Профиль активен'), default=True)
    is_staff = models.BooleanField(_('Доступ к админ-панели'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'phone_number', 'full_name']

    objects = UserManager()
    def __str__(self):
        return self.full_name
    def get_email(self):
        return self.email
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
    def get_advisor(self):
        return self.is_advisor
    def get_staff(self):
        return self.is_staff
    def get_active(self):
        return self.is_active
    def get_phone(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = '1. Пользователи'
        ordering = ['-is_superuser', '-is_advisor', '-is_teacher', 'full_name']
        
class Advisor(models.Model):
    user = models.ForeignKey("User", verbose_name=_("ID Пользователя"), on_delete=models.PROTECT, null=True)
    
    def get_control(self):
        return self.id
    def get_absolute_url(self):
        return reverse("advisor", kwargs={"pk": self.pk})
    
    @property
    def name(self):
        return self.user.full_name
    name.fget.short_description = 'ФИО'
    @property
    def email(self):
        return self.user.email
    email.fget.short_description = 'Email'
    @property
    def phone(self):
        return self.user.phone_number
    phone.fget.short_description = 'Номер телефона'
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Советника'
        verbose_name_plural = '2. Советники'
        ordering = ['id',]
        
class Form_e(models.Model):
    name = models.CharField(_("Форма обучения"), max_length=25, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Форму обучения'
        verbose_name_plural = 'Формы обучения'
        ordering = ['-name',]        

class Groups(models.Model):
    name = models.CharField(_("Наименование группы"), max_length=25)
    advisor = models.ForeignKey("Advisor", verbose_name=_("Советник"), on_delete=models.PROTECT, null=True)
    cours = models.IntegerField(_("Курс"), null=True)
    credit_price = models.IntegerField(_("Стоимость кредита"), null=True)
    form_of_e = models.ForeignKey("Form_e", verbose_name=_("Форма обучения"), on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = '4. Группы'
        ordering = ['-cours', '-name']

class Student(models.Model):
    cipher = models.CharField(_("Шифр студента"), max_length=25, unique=True)
    user = models.ForeignKey("User", verbose_name=_("Студент"), on_delete=models.PROTECT, null=True)
    groups = models.ForeignKey("Groups", verbose_name=_("Группа"), on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.cipher
    
    def get_student(self):
        return self.id
    
    @property
    def u_id(self):
        return self.user.id
    u_id.fget.short_description = 'ID Пользователя'
    @property
    def name(self):
        return self.user.full_name
    name.fget.short_description = 'ФИО'
    @property
    def course(self):
        return self.groups.cours
    course.fget.short_description = 'Курс'
    @property
    def email(self):
        return self.user.email
    email.fget.short_description = 'Email'
    @property
    def phone(self):
        return self.user.phone_number
    phone.fget.short_description = 'Номер телефона'
    @property
    def advisor(self):
        return self.groups.advisor
    advisor.fget.short_description = 'Академ советник'
    @property
    def credit_price(self):
        return self.groups.credit_price
    credit_price.fget.short_description = 'Стоимость кредита'
    @property
    def form_of_e(self):
        return self.groups.form_of_e
    form_of_e.fget.short_description = 'Форма обучения'
    
    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = '5. Студенты'
        ordering = ['-cipher', '-id']
        
class Teacher(models.Model):
    position = models.CharField(_("Должность"), max_length=50, null=True)
    user = models.ForeignKey("User", verbose_name=_("ID Пользователя"), on_delete=models.PROTECT, null=True)
    
    def get_control(self):
        return self.id
    def get_position(self):
        return self.position
    def get_absolute_url(self):
        return reverse("advisor", kwargs={"pk": self.pk})
    
    @property
    def name(self):
        return self.user.full_name
    name.fget.short_description = 'ФИО'
    @property
    def email(self):
        return self.user.email
    email.fget.short_description = 'Email'
    @property
    def phone(self):
        return self.user.phone_number
    phone.fget.short_description = 'Номер телефона'
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Преподавателя'
        verbose_name_plural = '3. Преподаватели'
        ordering = ['id',]