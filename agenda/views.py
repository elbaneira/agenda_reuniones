from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404 
from django.db.models import Q 
from django.utils import timezone
from django.contrib import messages  # <--- NUEVO: Para notificaciones en pantalla

from .forms import ReunionForm, TipoReunionForm 
from .models import Reunion, TipoReunion 


@login_required
def inicio(request):
    reuniones_usuario = Reunion.objects.filter(usuario=request.user)
    total_reuniones = reuniones_usuario.count()
    pendientes = reuniones_usuario.exclude(estado__iexact='CANCELADA').count()
    canceladas = reuniones_usuario.filter(estado__iexact='CANCELADA').count()
    total_tipos = TipoReunion.objects.count()
    
    ahora = timezone.now().date()
    proxima_reunion = reuniones_usuario.filter(
        fecha__gte=ahora
    ).exclude(
        estado__iexact='CANCELADA'
    ).order_by('fecha', 'hora').first()

    contexto = {
        'total_reuniones': total_reuniones,
        'pendientes': pendientes,
        'canceladas': canceladas,
        'total_tipos': total_tipos,
        'proxima_reunion': proxima_reunion,
    }
    
    return render(request, 'agenda/inicio.html', contexto)


@login_required 
def lista_reuniones(request): 
    reuniones = Reunion.objects.filter(usuario=request.user).order_by('fecha', 'hora') 
    tipos = TipoReunion.objects.all() 

    tipo_id = request.GET.get('tipo') 
    estado = request.GET.get('estado') 
    query = request.GET.get('q') 

    if tipo_id: 
        reuniones = reuniones.filter(tipo_id=tipo_id) 

    if estado: 
        reuniones = reuniones.filter(estado=estado) 

    if query:
        reuniones = reuniones.filter(
            Q(titulo__icontains=query) | Q(participantes__icontains=query)
        )

    contexto = { 
        'reuniones': reuniones, 
        'tipos': tipos, 
        'tipo_id': tipo_id, 
        'estado': estado, 
        'query': query, 
    } 
    return render(request, 'agenda/lista_reuniones.html', contexto) 


@login_required
def detalle_reunion(request, reunion_id):
    reunion = get_object_or_404(Reunion, id=reunion_id, usuario=request.user)
    return render(request, 'agenda/detalle_reunion.html', {'reunion': reunion})


@login_required 
def crear_reunion(request): 
    if request.method == 'POST': 
        form = ReunionForm(request.POST) 
        if form.is_valid(): 
            reunion = form.save(commit=False) 
            reunion.usuario = request.user 
            reunion.save() 
            messages.success(request, f"¡Reunión '{reunion.titulo}' creada exitosamente!")
            return redirect('lista_reuniones') 
    else: 
        form = ReunionForm() 

    return render(request, 'agenda/form_reunion.html', {'form': form, 'titulo': 'Nueva reunión'}) 


@login_required 
def editar_reunion(request, reunion_id): 
    reunion = get_object_or_404(Reunion, id=reunion_id, usuario=request.user) 

    if request.method == 'POST': 
        form = ReunionForm(request.POST, instance=reunion) 
        if form.is_valid(): 
            reunion_guardada = form.save() 
            messages.success(request, f"¡Reunión '{reunion_guardada.titulo}' actualizada correctamente!")
            return redirect('lista_reuniones') 
    else: 
        form = ReunionForm(instance=reunion) 

    return render(request, 'agenda/form_reunion.html', {'form': form, 'titulo': 'Editar reunión'}) 


@login_required 
def eliminar_reunion(request, reunion_id): 
    reunion = get_object_or_404(Reunion, id=reunion_id, usuario=request.user) 

    if request.method == 'POST': 
        titulo = reunion.titulo
        reunion.delete() 
        messages.warning(request, f"La reunión '{titulo}' ha sido eliminada.")
        return redirect('lista_reuniones') 

    return render(request, 'agenda/confirmar_eliminar.html', {'reunion': reunion})


# ==========================================
# --- CRUD COMPLETO TipoReunion -----
# ==========================================

@login_required
def lista_tipos(request):
    tipos = TipoReunion.objects.all()
    return render(request, 'agenda/lista_tipos.html', {'tipos': tipos})


@login_required
def crear_tipo(request):
    if request.method == 'POST':
        form = TipoReunionForm(request.POST)
        if form.is_valid():
            tipo = form.save()
            messages.success(request, f"Tipo de reunión '{tipo.nombre}' creado exitosamente.")
            return redirect('lista_tipos')
    else:
        form = TipoReunionForm()
    return render(request, 'agenda/form_tipo.html', {'form': form, 'titulo': 'Nuevo Tipo de Reunión'})


@login_required
def editar_tipo(request, tipo_id):
    tipo = get_object_or_404(TipoReunion, id=tipo_id)
    if request.method == 'POST':
        form = TipoReunionForm(request.POST, instance=tipo)
        if form.is_valid():
            tipo_guardado = form.save()
            messages.success(request, f"Tipo de reunión '{tipo_guardado.nombre}' actualizado.")
            return redirect('lista_tipos')
    else:
        form = TipoReunionForm(instance=tipo)
    return render(request, 'agenda/form_tipo.html', {'form': form, 'titulo': 'Editar Tipo de Reunión'})


@login_required
def eliminar_tipo(request, tipo_id):
    tipo = get_object_or_404(TipoReunion, id=tipo_id)
    if request.method == 'POST':
        nombre = tipo.nombre
        tipo.delete()
        messages.warning(request, f"Tipo de reunión '{nombre}' eliminado.")
        return redirect('lista_tipos')
    return render(request, 'agenda/confirmar_eliminar_tipo.html', {'tipo': tipo})