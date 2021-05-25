from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Manager():

    @classmethod
    def raise_not_found(cls):
        raise Exception(f'{cls._meta.verbose_name} not found')

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
        order_by = kwargs.get('order_by','name')
        name = kwargs.get('name', None)

        queryset = cls.objects.only('id', 'name')\
                   .order_by(order_by)

        if name:
            queryset = queryset.filter(
                name__unaccent__icontains=name)

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

        registry.owner = cls.validate_owner(data.get('owner'))
        registry.name = cls.validate_name(
            data.get('name'),
            owner = registry.owner,
            exclude = registry.id if registry else None
        )
        registry.address = cls.validate_address(data.get('address'))
        registry.phone = cls.validate_phone(data.get('phone'))
        registry.update_date = timezone.now()
        registry.save()
        return registry
