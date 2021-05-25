from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Manager():

    @classmethod
    def raise_not_found(cls):
        raise Exception(f'{cls._meta.verbose_title} not found')

    @classmethod
    def retrieve(cls, user, pizza, raise_not_found=False):
        ab = cls.objects.filter(user=user, pizza=pizza)
        if not ab:
            if raise_not_found:
                cls.raise_not_found()
            return None
        return ab.get()

    @classmethod
    def get_queryset(cls, **kwargs):
        order_by = kwargs.get('order_by','pizza')

        queryset = cls.objects.only('id', 'pizza')\
                   .order_by(order_by)

        pizza = kwargs.get('pizza', None)
        if pizza:
            if str(pizza).isdigit():
                queryset = queryset.filter(pizza__id=pizza)

        user = kwargs.get('user', None)
        if user:
            if str(user).isdigit():
                queryset = queryset.filter(user__id=pizza)

        return queryset

    @classmethod
    def perform_like(cls, data):
        user = cls.validate_user(data.get('user'))
        pizza = cls.validate_pizza(data.get('pizza'))

        registry = cls.retrieve(user=user, pizza=pizza)
        if registry:
            registry = registry.get()
        else:
            registry = cls()
            registry.pizza = pizza
            registry.user = user
            registry.registration_date = timezone.now()
            registry.save()
        return registry

    @classmethod
    def perform_deslike(cls, data):
        user = cls.validate_user(data.get('user'))
        pizza = cls.validate_pizza(data.get('pizza'))
        registry = cls.retrieve(user=user, pizza=pizza)
        if registry:
            registry.delete()
        return True
