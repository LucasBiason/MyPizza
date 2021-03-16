from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from src.utils.reflections import set_fields
from pizza.models.validators.likes import Validator
from pizza.models.managers.likes import Manager


class Likes(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    pizza = models.ForeignKey("pizza.Pizza", on_delete=models.CASCADE)

    class Meta:
        app_label = 'pizza'
