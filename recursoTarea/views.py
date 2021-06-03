from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaFormulario

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def vistaPrincipal(request):
    notas = Nota.objects.all()
    context ={
        'notas': notas
    }
    return render(request, 'nota/listarNotas.html', context)

def crearNota(request):
    formulario = NotaFormulario()
    if request.method == 'POST':
        formulario = NotaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarNotas')
    context = {
        "formulario": formulario
    }        
    return render(request, 'nota/agregarNota.html', context)

def buscarNota(request, idNota):
    notaEncontrada = None
    try:
        notaEncontrada = Nota.objects.get(pk = idNota) 
    except ObjectDoesNotExist:
        pass
    context = {
        "notaEncontrada": notaEncontrada
    }    
    return render(request, 'nota/producto.html', context)

def EdicionDeNota(request, idNota):
    notaEncontrada = None
    try:
        notaEncontrada = Nota.objects.get(pk = idNota)
    except ObjectDoesNotExist:
        pass
    formularioNota = NotaFormulario(instance= notaEncontrada)
    context = {
        'formulario': formularioNota,
        'nota': notaEncontrada
    }
    return render(request, 'nota/editar.html', context)  

def modificarNota(request, idNota):
    if request.method == 'POST':
        notaEncontrada = None
        try:
            notaEncontrada = Nota.objects.get(pk = idNota)
        except ObjectDoesNotExist: 
            pass
        formulario = NotaFormulario(request.POST, instance= notaEncontrada)
        if(formulario.is_valid()):
            formulario.save()
            return redirect('listarNotas')

def eliminarNota(request, idNota):
    notaEncontrada = None
    try:
        notaEncontrada = Nota.objects.get(pk = idNota)
        notaEncontrada.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('listarNotas')      
