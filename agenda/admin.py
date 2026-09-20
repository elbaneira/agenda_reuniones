from django.contrib import admin 
from .models import TipoReunion, Reunion 
 
@admin.register(TipoReunion) 
class TipoReunionAdmin(admin.ModelAdmin): 
    list_display = ('id', 'nombre') 
    search_fields = ('nombre',) 
 
 
@admin.register(Reunion) 
class ReunionAdmin(admin.ModelAdmin): 
    list_display = ('id', 'titulo', 'usuario', 'tipo', 'fecha', 'hora', 'estado') 
    list_filter = ('tipo', 'estado', 'fecha') 
    search_fields = ('titulo', 'lugar', 'participantes') 