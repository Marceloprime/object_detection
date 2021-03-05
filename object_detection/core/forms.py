from django import forms
from django.core.mail import  EmailMessage
from .models import PictureBase, PictureGoal


class PictureBaseForm(forms.ModelForm):
    class Meta:
        model = PictureBase
        fields = ['id','imagem']

class PictureGoalForm(forms.ModelForm):
    class Meta:
        model = PictureGoal
        fields = ['id','imagem']