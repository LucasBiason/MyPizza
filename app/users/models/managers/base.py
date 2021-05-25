from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """ Create and saves the new user """
        if not username:
            raise ValueError(_("User must have username"))
        user = self.model(
            username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """ Create and saves the new superuser """
        user = self.create_user(username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

