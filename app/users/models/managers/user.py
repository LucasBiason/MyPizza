from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError

from src.utils import file_system


class Manager():

    @classmethod
    def raise_not_found(cls):
        raise Exception(f'{cls._meta.verbose_name} not found')

    @classmethod
    def retrieve(cls, user_pk, **kwargs):
        try:
            if str(user_pk).isdigit():
                users = cls.objects.filter(pk=user_pk)
            else:
                users = cls.objects.filter(username=user_pk)
            if kwargs.get('exclude'):
                users = users.exclude(pk=kwargs['exclude'])
            return users.get()
        except Exception:
            if 'silence' in kwargs:
                return None
            raise Exception('USER NOT FOUND')

    @classmethod
    def get_queryset(cls, **kwargs):
        queryset = cls.objects.all()
        logged_user = kwargs.get('logged_user')

        if not logged_user or not logged_user.is_staff:
            raise PermissionDenied('USER TYPE NOT ALLOWED')

        if kwargs.get('is_staff'):
            queryset = queryset.filter(is_staff=True)

        if kwargs.get('is_owner'):
            queryset = queryset.filter(is_owner=True)

        email = kwargs.get('email')
        if email:
            queryset = queryset.filter(email=email)

        username = kwargs.get('username')
        if username:
            queryset = queryset.filter(username=username)

        first_name = kwargs.get('first_name')
        if first_name:
            queryset = queryset.filter(
                first_name__unaccent__icontains=first_name)

        last_name = kwargs.get('last_name')
        if last_name:
            queryset = queryset.filter(
                last_name__unaccent__icontains=last_name)

        if kwargs.get('order_by'):
            queryset = queryset.order_by(kwargs.get('order_by'))

        return queryset

    @classmethod
    def perform_create(cls, data, user_creator=None):
        cls.validate_can_manage(user_creator)
        data['is_active'] = True
        user = cls._set_data_and_save(data, user_creator=user_creator)
        return user

    def perform_update(self, data, user_creator=None):
        self.validate_can_manage(user_creator)
        data['id'] = self.id
        data['is_active'] = True
        self._set_data_and_save(data, user=self,
                                user_creator=user_creator)
        return self

    @classmethod
    def _set_data_and_save(cls, data, user=None, user_creator=None):
        username = cls.validate_username(
            data.get('username'),
            exclude=user.id if user else None
        )

        if not user:
            user = cls.retrieve(username, silence=True)
            if not user:
                user = cls()
                if not data.get('password'):
                    raise ValidationError('Password required.')

        user.username = username
        user.email = cls.validate_email(
            data.get('email'),
            exclude=user.id if user else None
        )
        user.first_name = cls.validate_first_name(data.get('first_name'))
        user.last_name = cls.validate_last_name(data.get('last_name'))
        user.is_staff = cls.validate_is_staff(data.get('is_staff'),
                                              user_creator=user_creator)
        user.is_owner = cls.validate_is_owner(data.get('is_owner'),
                                              user_creator=user_creator)

        password = cls.validate_password(data.get('password'), register=user)
        if password:
            user.set_password(password)

        user.save()
        return user
