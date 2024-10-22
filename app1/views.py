from django.shortcuts import render
from app1.forms import FormMascota
from app1.models import MascotaM

# Create your views here.


def index(request):
    return render(request,'app1/index.html')


def agregarMascota(request):
    form = MascotaM()
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


# def actualizarMascota(request):


# def eliminarMascota (request):
