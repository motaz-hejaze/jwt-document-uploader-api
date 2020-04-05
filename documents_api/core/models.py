from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
            Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True , db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True , blank=True)
    updated_at = models.DateTimeField(auto_now=True , blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return "{}".format(self.email)


class Metadata(models.Model):
    name = models.CharField(max_length=200)
    string = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True , blank=True)
    updated_at = models.DateTimeField(auto_now=True , blank=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True , blank=True)
    updated_at = models.DateTimeField(auto_now=True , blank=True)

    def __str__(self):
        return self.name