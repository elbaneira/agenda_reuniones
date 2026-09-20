from django.contrib.auth.models import User 
from django.db import models
 
 
class TipoReunion(models.Model): 
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField(blank=True) 
 
    def __str__(self): 
        return self.nombre 
 
 
class Reunion(models.Model): 
    ESTADOS = [ 
        ('pendiente', 'Pendiente'), 
        ('realizada', 'Realizada'), 
        ('cancelada', 'Cancelada'), 
    ] 
 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    tipo = models.ForeignKey(TipoReunion, on_delete=models.PROTECT) 
    titulo = models.CharField(max_length=150) 
    fecha = models.DateField() 
    hora = models.TimeField() 
    lugar = models.CharField(max_length=150) 
    participantes = models.TextField() 
    observaciones = models.TextField(blank=True) 
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente') 
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return self.titulo 