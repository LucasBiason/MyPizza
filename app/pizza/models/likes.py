from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from utils.reflections import set_fields
from pizza.models.validators.likes import Validator
from pizza.models.managers.likes import Manager


class Likes(models.Model, Validator, Manager):

    user = models.ForeignKey(
        "users.User",
        verbose_name = _('User'),
        on_delete=models.CASCADE
    )

    pizza = models.ForeignKey(
        "pizza.Pizza",
        verbose_name = _('Pizza'),
        on_delete=models.CASCADE
    )

    registration_date = models.DateTimeField(
        verbose_name = _('Registration'),
        default = timezone.now
    )
    class Meta:
        app_label = 'pizza'
