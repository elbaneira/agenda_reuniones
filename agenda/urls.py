from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reuniones/', views.lista_reuniones, name='lista_reuniones'),  # <--- Esta es la URL correcta
    path('reuniones/crear/', views.crear_reunion, name='crear_reunion'),
    path('reuniones/<int:reunion_id>/', views.detalle_reunion, name='detalle_reunion'),
    path('reuniones/editar/<int:reunion_id>/', views.editar_reunion, name='editar_reunion'),
    path('reuniones/eliminar/<int:reunion_id>/', views.eliminar_reunion, name='eliminar_reunion'),
    
    # Rutas para TipoReunion
    path('tipos/', views.lista_tipos, name='lista_tipos'),
    path('tipos/crear/', views.crear_tipo, name='crear_tipo'),
    path('tipos/editar/<int:tipo_id>/', views.editar_tipo, name='editar_tipo'),
    path('tipos/eliminar/<int:tipo_id>/', views.eliminar_tipo, name='eliminar_tipo'),
]