from django.contrib import admin
from .models import PictureBase, PictureGoal, GameBase
# Register your models here.

admin.site.register(PictureBase)
admin.site.register(PictureGoal)
admin.site.register(GameBase)
