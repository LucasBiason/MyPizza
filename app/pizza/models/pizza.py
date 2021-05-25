from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from utils.reflections import set_fields
from pizza.models.validators.pizza import Validator
from pizza.models.managers.pizza import Manager


class Pizza(models.Model, Validator, Manager):

    title = models.CharField(
        verbose_name = _('Title'),
        max_length=120
    )

    description = models.CharField(
        verbose_name = _('Description'),
        max_length=240
    )

    thumbnail_url = models.URLField(
        verbose_name = _('Photo URL'),
        blank=True, null=True
    )

    approved = models.BooleanField(
        verbose_name = _('Approved'),
        default=False
    )

    creator = models.ForeignKey(
        "pizza.Pizzeria",
        verbose_name = _('Pizzeria'),
        on_delete=models.CASCADE
    )

    registration_date = models.DateTimeField(
        verbose_name = _('Registration'),
        default = timezone.now
    )

    update_date = models.DateTimeField(
        verbose_name = _('Update'),
        default = timezone.now
    )
    class Meta:
        app_label = 'pizza'

    def __str__(self):
        return self.title
