
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from src.utils import validators


class Validator():

    @classmethod
    def validate_owner(cls, owner_id):
        from user.models import UserProfile
        return UserProfile.validate_registry(owner_id, required=True)

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
            raise ValidationError(_(f'{cls._meta.verbose_name} já criada'))
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
    def validate_registry(cls, registry, required=False, only_retrieve=False):
        if not required and not registry:
            return None

        if required and not registry:
            raise ValidationError(_(f'{cls._meta.verbose_name} obrigatória'))

        registry = cls.get_or_create(
            registry,
            only_retrieve=only_retrieve
        )
        if not registry or not registry.id:
            raise ValidationError(_(f'{cls._meta.verbose_name} inválida'))
        return registry
