import secrets

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from email_validator import validate_email as validate, EmailNotValidError



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is a required field.')
        if not password:
            raise ValueError('Password is a required field.')

        try:
            valid = validate(email)
            email = valid.normalized
        except EmailNotValidError as e:
            raise ValueError(str(e))

        if CustomUser.objects.filter(email=email).exists():
            raise ValueError('Email already registered.')

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False, max_length=255, verbose_name='Email')
    password = models.CharField(max_length=155, verbose_name='Contraseña')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    is_active = models.BooleanField(default=True, verbose_name="¿El usuario está activo?")
    is_superuser = models.BooleanField(default=False, verbose_name="¿Es administrador?")
    is_staff = models.BooleanField(default=False, verbose_name="Autorizado para ser staff")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while CustomUser.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"