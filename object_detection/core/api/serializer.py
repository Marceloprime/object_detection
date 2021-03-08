from core.models import GameBase
from rest_framework import serializers
from rest_framework.response import Response

class GameBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameBase
        fields = '__all__'