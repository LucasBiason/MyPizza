from rest_framework import mixins, viewsets, authentication, permissions
from rest_framework.response import Response

from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator

from users.decorators import administrator_required
from pizza.models import Pizza
from pizza.serializers import PizzaSerializer


class ManagePizzaView(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin):
    ''' Manage Pizzas endpoints'''
    model = Pizza
    serializer_class = PizzaSerializer
    authentication_classes =(authentication.TokenAuthentication,)
    permission_classes =(permissions.IsAuthenticated,)
    queryset = Pizza.objects.all()

    def get_queryset(self, *args, **kwargs):
        data = dict(self.request.query_params.items())
        data['user'] = self.request.user
        return self.model.get_queryset(**data)

    def _get_registry(self, pk):
        registry = self.model.retrieve(pk, raise_not_found=True)
        return registry

    def retrieve(self, request, *args, **kwargs):
        registry = self._get_registry(kwargs.get('pk'))
        return Response(self.serializer_class(registry).data)

    @method_decorator(administrator_required())
    def destroy(self, request, *args, **kwargs):
        registry = self._get_registry(kwargs.get('pk'))
        registry.delete()
        return Response({ 'status': 'success'})

    @method_decorator(administrator_required())
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        registry = self.model.perform_create(data)
        return Response(self.serializer_class(registry).data)

    @method_decorator(administrator_required())
    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        registry = self._get_registry(kwargs.get('pk'))
        registry.perform_update(data)
        return Response(self.serializer_class(registry).data)
