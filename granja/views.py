from django.shortcuts import render
from .models import Animal

def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, 'granja/lista_animais.html', {'animais': animais})
