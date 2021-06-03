from enum import Flag
from django.db import models
from django.forms import widgets
from django import forms
# Create your models here.
class Nota(models.Model):
    titulo_nota = models.CharField('Nombre Del recordatorio',
        max_length= 50,
        blank= False,
        null= False
    )
    descripcion_nota = models.CharField('Descripcion Del recordatorio',
        max_length= 200,
        blank= False,
        null= False
    )
    fecha_creacion = models.DateTimeField('Fecha de creacion Del recordatorio',
        auto_now= True
    )
    fecha_fin = models.DateTimeField('Fecha fin Del recordatorio',
        blank= False,
        null= False
    )
    estado_nota = models.CharField('Estado Del recordatorio Vigente / Vencida / Completada',
        max_length= 30,
        blank= False,
        null= False
    )