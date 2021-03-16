from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from src.utils import validators


class Validator():

    @classmethod
    def validate_can_manage(cls, user_creator=None):
        if user_creator \
            and not user_creator.is_superuser\
            and not user_creator.is_staff:
            raise ValidationError('Logged in user does not have permission to manage users')
        return True

    @classmethod
    def validate_username(cls, username, exclude=None):
        if cls.retrieve(username, exclude=exclude, silence=True):
            raise ValidationError('User already created.')

        username = validators.validate_text(
            username, required=True,
            max_length=cls.username_max_length,
            verbose=cls.username_verbose
        )
        return username

    @classmethod
    def validate_password(cls, password, register=None):
        password = validators.validate_text(
            password,
            required=not register, # Only required with new user
            max_length=cls.password_max_length,
            verbose=cls.password_verbose
        )
        return password

    @classmethod
    def validate_is_staff(cls, is_staff, user_creator=None):
        if not is_staff:
            return False
        if not user_creator:
            raise ValidationError('User without permission.')
        return is_staff

    @classmethod
    def validate_is_owner(cls, is_owner, user_creator=None):
        if not is_owner:
            return False
        if not user_creator:
            raise ValidationError('User without permission.')
        return is_owner

    @classmethod
    def validate_first_name(cls, first_name):
        first_name = validators.validate_text(
            first_name, required=True,
            max_length=cls.first_name_max_length,
            verbose=cls.first_name_verbose
        )
        return first_name

    @classmethod
    def validate_last_name(cls, last_name):
        last_name = validators.validate_text(
            last_name, required=True,
            max_length=cls.last_name_max_length,
            verbose=cls.last_name_verbose
        )
        return last_name

    @classmethod
    def validate_email(cls, email, exclude=None):
        email = validators.validate_email(
            email, required=True,
            max_length=cls.email_max_length,
            verbose=cls.email_verbose
        )
        search = cls.objects.only('email').filter(
            email=email
        )
        if exclude:
            search = search.exclude(pk=exclude)
        if search:
            raise ValidationError(_('E-mail in use by another register'))
        return email or ''

    @classmethod
    def validate_registry(cls, registry, required=False):
        if not required and not registry:
            return None

        if required and not registry:
            raise ValidationError(_(f'{cls._meta.verbose_name} required'))

        registry = cls.retrieve(registry)
        if not registry.id:
            raise ValidationError(_(f'{cls._meta.verbose_name} invalid'))
        return registry
