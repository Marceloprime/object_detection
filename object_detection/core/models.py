from django.db import models
from stdimage.models import StdImageField
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

def upload_image_info(instance,filename):
    return f"{instance.id}-{filename}"

ACTION_CHOICES= (
    ('GRAYSCALE', 'grayscale'),
)

class GameBase(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de atualização', auto_now=True)
    imagemBase = models.ImageField(upload_to=upload_image_info,blank=False)
    imagemGoal = models.ImageField(upload_to=upload_image_info,blank=False)
    imageAnswer = models.ImageField(upload_to=upload_image_info,blank=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES,default='GRAYSCALE')

    def __str__(self):
        return str(self.id)

    
    def save(self, *args, **kwargs):
        width = self.imagemGoal.width
        height = self.imagemGoal.height
        # open image
        pil_img = Image.open(self.imagemBase)
        pil_img2 = Image.open(self.imagemGoal)
        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        cv_img2 = np.array(pil_img2)
        
        img = get_filtered_image(cv_img, cv_img2, self.action, width, height)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.imageAnswer.save(str(self.imageAnswer), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)

class ImageModel(models.Model):
    image = models.FileField(upload_to=upload_image_info)
