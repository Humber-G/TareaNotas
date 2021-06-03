from django.urls import path
from .views import vistaPrincipal, crearNota, buscarNota, EdicionDeNota, modificarNota, eliminarNota

urlpatterns = [
    path('', vistaPrincipal, name= 'listarNotas'),
    path('agregar/',crearNota, name= 'agregarNota'),
    path('buscar/<int:idNota>', buscarNota, name= 'buscarNota'),
    path('editar/<int:idNota>', EdicionDeNota, name= 'edicion'),
    path('modificar/<int:idNota>', modificarNota, name= 'modificar'),
    path('eliminar/<int:idNota>', eliminarNota, name= 'eliminar')
]