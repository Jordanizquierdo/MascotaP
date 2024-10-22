from django.shortcuts import render,redirect
from app1.forms import FormMascota
from app1.models import MascotaM

# Create your views here.


def index(request):
    return render(request,'app1/index.html')



def agregarMascota(request):
    form = FormMascota()
    if request.method == 'POST':
        form = FormMascota(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'app1/agregar.html',data)


def listadoMascotas(request):
    mascotas = MascotaM.objects.all()
    data = {'mascotas':mascotas}
    return render(request,'app1/mascotas.html',data)

def actualizarMascota(request,id):
    mascota = MascotaM.objects.get(id = id)
    form = FormMascota (instance=mascota)
    if request.method == 'POST':
        form = FormMascota(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'app1/agregar.html',data)


def eliminarMascota (request,id):
    mascota = MascotaM.objects.get(id = id)
    mascota.delete()
    return redirect('/mascotas')
