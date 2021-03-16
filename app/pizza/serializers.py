from rest_framework import serializers

from pizza.models import Pizza, Pizzeria, Likes
from user.serializers import UserProfileSerializer


class PizzaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pizza
        fields = ('id', 'title', 'description')


class PizzeriaSerializer(serializers.HyperlinkedModelSerializer):

    owner = UserProfileSerializer()

    class Meta:
        model = Pizzeria
        fields = ('id', 'name', 'address', 'phone', 'owner')
