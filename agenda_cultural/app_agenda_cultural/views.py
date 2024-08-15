from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventoForm()
    
    return render(request, 'criar_evento.html', {'form': form})

def home(request):
    eventos = Evento.objects.all()
    return render(request, 'home.html', {'eventos': eventos})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('home')
    return redirect('home')