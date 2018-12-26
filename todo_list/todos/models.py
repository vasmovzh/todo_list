from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20, blank=True, default='')
    content = models.TextField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', 'updated',)


class Company(models.Model):
    company_name = models.CharField(max_length=20, blank=True, default='company')
    #employee = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)

    class Meta:
        ordering = ('company_name',)

    def __str__(self):
        return self.company_name

"""
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        \"""
        Create and save a new user with the given parameters
        :param email:
        :param username:
        :param password:
        :param extra_fields:
        :return:
        \"""
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_('username'), max_length=50, unique=True, validators=[username_validator],)
    email = models.EmailField(_('email adress'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    #companies = ArrayField(models.CharField(max_length=20))
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_full_name(self):
        full_name = '%s  %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.username
"""

# Create your models here.
