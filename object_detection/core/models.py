import cv2
import numpy as np
from matplotlib import pyplot as plt

from django.db import models
from stdimage.models import StdImageField

#Signals
from django.db.models import signals #permite realizar processos entre o processo de salvamento no banco de dados
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de atualização', auto_now=True)
    height = models.DecimalField('height', max_digits=15, decimal_places=5, blank=True, null=True)
    width = models.DecimalField('width', max_digits=15, decimal_places=5, blank=True, null=True)

    class Meta:
        abstract = True

class PictureBase(Base):
    imagem = StdImageField('imagem', upload_to='picturebase', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return str(self.id)

    def match_picture(self, PictureGoal):
        print('Teste')


def picturebase_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.id)

signals.pre_save.connect(picturebase_pre_save,sender=PictureBase)

class PictureGoal(Base):
    imagem = StdImageField('imagem', upload_to='picturegoal', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return str(self.id)

def picturegoal_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.id)

signals.pre_save.connect(picturegoal_pre_save,sender=PictureGoal)