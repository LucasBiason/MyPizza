from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from src.utils.reflections import set_fields
from pizza.models.validators.pizza import Validator
from pizza.models.managers.pizza import Manager


class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey("pizza.Pizzeria", on_delete=models.CASCADE)

    class Meta:
        app_label = 'pizza'

    def __str__(self):
        return self.title
