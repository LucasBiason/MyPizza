from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from utils.reflections import set_fields
from pizza.models.validators.pizzeria import Validator
from pizza.models.managers.pizzeria import Manager


class Pizzeria(models.Model, Validator, Manager):

    owner = models.ForeignKey(
        "users.User",
        verbose_name = _('Owner'),
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name = _('Name'),
        max_length=240
    )

    address = models.CharField(
        verbose_name = _('Address'),
        max_length=512
    )

    phone = models.CharField(
        verbose_name = _('Phone'),
        max_length=40
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
        ordering = ['name']
        get_latest_by = 'id'
        verbose_name =_('Pizzeria')
        verbose_name_plural =_('Pizzerias')

    def __str__(self):
        return self.name

    @property
    def pizzas(self):
        from pizza.models import Pizza
        return Pizza.get_queryset(creator=self)

Pizzeria = set_fields(Pizzeria)
