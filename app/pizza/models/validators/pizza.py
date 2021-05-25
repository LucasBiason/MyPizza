
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from utils import validators


class Validator():

    @classmethod
    def validate_creator(cls, creator_id):
        from pizza.models import Pizzeria
        return Pizzeria.validate_registry(creator_id, required=True)

    @classmethod
    def validate_title(cls, title, creator=None, exclude=None):
        title = validators.validate_text(
            title, required=True,
            max_length=cls.title_max_length,
            verbose=cls.title_verbose
        )
        search = cls.objects.only('title').filter(
                title__unaccent__iexact=title,
                creator=creator
        )
        if exclude:
            search = search.exclude(pk=exclude)
        if search:
            raise ValidationError(_(f'{cls._meta.verbose_name} already created.'))
        return title

    @classmethod
    def validate_description(cls, description):
        description = validators.validate_text(
            description, required=True,
            max_length=cls.description_max_length,
            verbose=cls.description_verbose,
            only_digits=True
        )
        return description or ''

    @classmethod
    def validate_thumbnail_url(cls, thumbnail_url):
        thumbnail_url = validators.validate_url(
            thumbnail_url, required=True,
            max_length=cls.thumbnail_url_max_length,
            verbose=cls.thumbnail_url_verbose
        )
        return thumbnail_url or ''

    @classmethod
    def validate_approved(cls, approved):
        approved = validators.validate_boolean(
            approved, required=True,
            max_length=cls.approved_max_length,
            verbose=cls.approved_verbose
        )
        return approved or ''

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
