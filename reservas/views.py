from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import Reserva_Formulario

# Create your views here.

def ver_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/ver_reservas.html', {'reservas': reservas})

def agregar_reserva(request):
    if request.method == 'POST':
        form = Reserva_Formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_reservas')
    else:
        form = Reserva_Formulario()
    return render(request, 'reservas/agregar_reserva.html', {'form': form})

def modificar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = Reserva_Formulario(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('ver_reservas')
    else:
        form = Reserva_Formulario(instance=reserva)
    return render(request, 'reservas/modificar_reserva.html', {'form': form, 'reserva': reserva})

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('ver_reservas')
