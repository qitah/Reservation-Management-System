from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    employee_number = models.CharField(_('employee number'),max_length=5 ,unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'employee_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
