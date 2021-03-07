from core.models import GameBase, PictureGoal, PictureBase
from rest_framework import serializers


class GameBaseSerializer(serializers.Serializer):
    imagemBase = serializers.ImageField()
    imagemGoal = serializers.ImageField()

    def create(self, validated_data, request):
        return GameBase.objects.create(**validated_data)