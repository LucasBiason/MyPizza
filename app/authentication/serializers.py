from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from users.models import User


class AuthTokenSerializer(serializers.Serializer):
    ''' Serializer for the user authentication object '''
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        ''' validate and authenciate the user '''
        username = attrs.get('username')
        password = attrs.get('password')

        search_user = User.objects.filter(email=username)
        if search_user:
            username = search_user.username

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg =_('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
