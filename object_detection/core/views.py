from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  PictureBaseForm, PictureGoalForm
from .models import  PictureBase, PictureGoal

# Create your views here.
def index(request):
    if str(request.method) == 'POST':
        form = PictureBaseForm(request.POST, request.FILES)
        formgoal = PictureGoalForm(request.POST, request.FILES)

        if form.is_valid() and formgoal.is_valid():
            form.save()
            form = PictureBaseForm()
            formgoal.save()
            formgoal = PictureGoalForm()
        else:
            messages.error(request, 'Erro ao enviar imagem')
    else:
        form = PictureBaseForm()
        formgoal = PictureGoalForm()

    context = {
        'form': form,
        'formgoal': formgoal,
        'PictureBase' : PictureBase
    }
    return render(request, 'index.html', context)

