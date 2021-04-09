from rest_framework import serializers

from pizza.models import Likes
from users.serializers import UserSerializer


class LikesSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Likes
        fields = ('id', 'user')
