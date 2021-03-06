
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from utils import validators


class Validator():

    @classmethod
    def validate_owner(cls, owner_id):
        from user.models import User
        return User.validate_registry(owner_id, required=True)

    @classmethod
    def validate_name(cls, name, owner=None, exclude=None):
        name = validators.validate_text(
            name, required=True,
            max_length=cls.name_max_length,
            verbose=cls.name_verbose
        )
        search = cls.objects.only('name').filter(
                name__unaccent__iexact=name,
                owner=owner
        )
        if exclude:
            search = search.exclude(pk=exclude)
        if search:
            raise ValidationError(_(f'{cls._meta.verbose_name} already created.'))
        return name

    @classmethod
    def validate_address(cls, address):
        address = validators.validate_text(
            address, required=True,
            max_length=cls.address_max_length,
            verbose=cls.address_verbose,
            only_digits=True
        )
        return address or ''

    @classmethod
    def validate_phone(cls, phone):
        phone = validators.validate_text(
            phone, required=True,
            max_length=cls.phone_max_length,
            verbose=cls.phone_verbose,
            only_digits=True
        )
        return phone or ''

    @classmethod
    def validate_registry(cls, registry, required=False, only_retrieve=False):
        if not required and not registry:
            return None

        if required and not registry:
            raise ValidationError(_(f'{cls._meta.verbose_name} required'))

        registry = cls.retrieve(registry)
        if not registry or not registry.id:
            raise ValidationError(_(f'{cls._meta.verbose_name} invalid'))
        return registry
