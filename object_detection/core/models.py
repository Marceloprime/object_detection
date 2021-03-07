import cv2
import numpy as np
from matplotlib import pyplot as plt

from django.db import models
from stdimage.models import StdImageField

def upload_image_info(instance,filename):
    return f"{instance.id}-{filename}"


class GameBase(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de atualização', auto_now=True)
    imagemBase = models.ImageField(upload_to=upload_image_info,blank=False)
    imagemGoal = models.ImageField(upload_to=upload_image_info,blank=False)
    def __str__(self):
        return str(self.id)


class PictureGoal(models.Model):
    imagem = models.ImageField(upload_to=upload_image_info,blank=False)
    def __str__(self):
        return str(self.id)
        
class PictureBase(models.Model):
    imagem = models.ImageField(upload_to=upload_image_info,blank=False)

    def __str__(self):
        return str(self.id)

    def match_picture(self, PictureGoal):
        print('Teste')




