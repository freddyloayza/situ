from django.shortcuts import render
from .forms import PasajeroFormulario
from .models import Pasajero
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request,"index.html",{})

def pasajeros(request):
    data = PasajeroFormulario()    
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

    return render(request,"pasajeros.html",{"pasajeros":pasajeros, 'form':data})

def pasajerosEdit(request, id):
    pasajeros = get_object_or_404(Pasajero, id = id)
    data = {
        'form' : PasajeroFormulario(instance=pasajeros)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajeros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pasajero editado')
            return redirect(to="pasajeros")
            
    return render(request,'pasajerosEdit.html',data)

def pasajerosDelete(request, id):
   # formulario = PasajeroFormulario.objects.get(id=id)
    pasajeros = get_object_or_404(Pasajero, id = id)
    pasajeros.delete()
    messages.success(request, 'Pasajero eliminado')
    return redirect(to="pasajeros")