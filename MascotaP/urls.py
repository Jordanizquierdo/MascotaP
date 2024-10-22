
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mascotas/', views.listadoMascotas),
    path('agregar/', views.agregarMascota),
    path('actualizarMascota/<int:id>/',views.actualizarMascota),
    path('eliminarMascota/<int:id>/',views.eliminarMascota)
]
