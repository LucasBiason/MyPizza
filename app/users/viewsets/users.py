from rest_framework import mixins, viewsets, authentication, permissions
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from users.decorators import administrator_required
from users.models import User
from users.serializers import UserSerializer


class ManageUserView(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin):
    ''' Manage the authenticated user '''
    model = User
    serializer_class = UserSerializer
    authentication_classes =(authentication.TokenAuthentication,)
    permission_classes =(permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        data = dict(self.request.query_params.items())
        data['logged_user'] = self.request.user
        return User.get_queryset(**data)

    def _get_registry(self, pk):
        registry = self.model.retrieve(pk)
        if not registry.id:
            registry.raise_not_found()
        return registry

    @method_decorator(administrator_required())
    def retrieve(self, request, *args, **kwargs):
        user = self._get_registry(kwargs.get('pk'))
        return Response(self.serializer_class(user).data)

    @method_decorator(administrator_required())
    def destroy(self, request, *args, **kwargs):
        user = self._get_registry(kwargs.get('pk'))
        user.is_active = False
        user.save()
        return Response({
            'user': kwargs.get('pk'),
            'status': 'success'
        })

    @method_decorator(administrator_required())
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        user = User.perform_create(data, user_creator=self.request.user)
        return Response(self.serializer_class(user).data)

    @method_decorator(administrator_required())
    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        user = self._get_registry(kwargs.get('pk'))
        user.perform_update(data, user_creator=self.request.user)
        return Response(self.serializer_class(user).data)


