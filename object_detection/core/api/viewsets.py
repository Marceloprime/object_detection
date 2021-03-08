from core.models import GameBase
from .serializer import  GameBaseSerializer
from rest_framework.viewsets import  ModelViewSet

from rest_framework.decorators import action

from django.http import HttpResponse


class ImageViewSet(ModelViewSet):
    queryset = GameBase.objects.all()
    serializer_class = GameBaseSerializer

    @action(methods=['get'],detail=False)
    def answer(self, request):
        img = GameBase.objects.latest('id')
        
        answer = img.imageAnswer

        return HttpResponse(answer, content_type="image/png")