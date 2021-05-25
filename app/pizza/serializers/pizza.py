from rest_framework import serializers

from pizza.models import Pizza

from .likes import LikesSerializer


class PizzaSerializer(serializers.ModelSerializer):

    likes = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ('id', 'title', 'description', 'likes')

    def get_likes(self, obj):
        if not obj.likes:
            return []
        return LikesSerializer(obj.likes, many=True).data
