from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Manager():

    @classmethod
    def raise_not_found(cls):
        raise Exception(f'{cls._meta.verbose_title} not found')

    @classmethod
    def retrieve(cls, id, raise_not_found=False):
        ab = cls.objects.filter(pk=id)
        if not ab:
            if raise_not_found:
                cls.raise_not_found()
            return cls()
        return ab.get()

    @classmethod
    def get_queryset(cls, **kwargs):
        order_by = kwargs.get('order_by','title')

        queryset = cls.objects.only('id', 'title')\
                   .order_by(order_by)

        title = kwargs.get('title', None)
        if title:
            queryset = queryset.filter(
                title__unaccent__icontains=title)

        creator = kwargs.get('creator', None)
        if creator:
            queryset = queryset.filter(creator=creator)

        return queryset

    @classmethod
    def perform_create(cls, data):
        return cls._set_data_and_save(data)

    def perform_update(self, data):
        data['id'] = self.id
        self._set_data_and_save(data, registry=self)
        return self

    @classmethod
    def _set_data_and_save(cls, data, registry=None):
        if not registry:
            registry = cls()
            registry.registration_date = timezone.now()

        registry.creator = cls.validate_creator(data.get('creator'))
        registry.title = cls.validate_title(
            data.get('title'),
            creator = registry.creator,
            exclude = registry.id if registry else None
        )
        registry.description = cls.validate_description(data.get('description'))
        registry.thumbnail_url = cls.validate_thumbnail_url(data.get('thumbnail_url'))
        registry.approved = cls.validate_approved(data.get('approved'))
        registry.update_date = timezone.now()
        registry.save()
        return registry

    @property
    def likes(self):
        from pizza.models import Likes
        return Likes.get_queryset(pizza=self)

    def like(self, user):
        from pizza.models import Likes
        return Likes.perform_like({'pizza': self, 'user': user})

    def has_like(self, user):
        from pizza.models import Likes
        return Likes.retrieve(user, self)

    def deslike(self, user):
        from pizza.models import Likes
        return Likes.perform_deslike({'pizza': self, 'user': user})
