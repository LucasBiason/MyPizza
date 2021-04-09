from rest_framework import serializers

from pizza.models import Pizza, Pizzeria, Likes
from users.serializers import UserSerializer

from .pizza import PizzaSerializer


class PizzeriaSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    pizzas = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = ('id', 'name', 'address', 'phone', 'owner', 'pizzas')

    def get_pizzas(self, obj):
        if not obj.pizzas:
            return []
        return PizzaSerializer(obj.pizzas, many=True).data
