from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _

from src.utils.models.reflections import set_fields
from users.models.validators.user import Validator
from users.models.managers.base import UserManager
from users.models.managers.user import Manager


class User(AbstractBaseUser, PermissionsMixin, Manager, Validator):
    """ Custom user models that suppors using username instead of username """

    username = models.CharField(
        verbose_name = _('Username'),
        max_length=100,
        unique=True, blank=False
    )

    is_active = models.BooleanField(
        verbose_name = _('Active'),
        default=True
    )

    is_staff = models.BooleanField(
       verbose_name = _('Staff'),
       default=False
    )

    is_superuser = models.BooleanField(
        verbose_name = _('Super User'),
        default=False
    )

    is_owner = models.BooleanField(
       verbose_name = _('Pizzeria Owner'),
       default=False
    )

    first_name = models.CharField(
        verbose_name = _('First Name'),
        max_length=30,
        default=''
    )

    last_name = models.CharField(
        verbose_name = _('Last Name'),
        max_length=100,
        default=''
    )

    email = models.EmailField(
        verbose_name = _('E-mail'),
        max_length = 100,
        blank = False,
        null = False
    )

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.name

    @property
    def name(self):
        return ' '.join([self.first_name, self.last_name])

User = set_fields(User)
