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
    is_advisor = models.BooleanField(_('Академический советник'), default=False)
    is_active = models.BooleanField(_('Профиль активен'), default=True)
    is_staff = models.BooleanField(_('Доступ к админ-панели'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'phone_number', 'full_name']

    objects = UserManager()
    def __str__(self):
        return self.email
    def get_short_name(self):
        return self.full_name
    def get_full_name(self):
        return self.full_name
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['is_superuser', 'is_advisor', 'full_name']