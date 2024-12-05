from django.shortcuts import render, redirect
from .models import Reparacion
# Create your views here.
def reparaciones(request):
    lasreparaciones = Reparacion.objects.all()
    return render(request, 'gestionarReparaciones.html', {"misreparaciones": lasreparaciones})

def registrarReparacion(request):
    id = request.POST["txtid"]
    fecha = request.POST["numfecha"]
    id_reloj = request.POST["numid_reloj"]
    descripcion_problema = request.POST["txtdescripcion_problema"]
    costo_de_reparacion = request.POST["numcosto_de_reparacion"]
    tiempo_de_reparacion = request.POST["txttiempo_de_reparacion"]
    estado_reparacion = request.POST["txtestado_reparacion"]

    guardarReparacion = Reparacion.objects.create(
        id = id,
        fecha = fecha,
        id_reloj = id_reloj,
        descripcion_problema = descripcion_problema,
        costo_de_reparacion = costo_de_reparacion,
        tiempo_de_reparacion = tiempo_de_reparacion,
        estado_reparacion = estado_reparacion,
    ) 
    return redirect("reparaciones")

def seleccionarReparacion(request, id):
    reparacion = Reparacion.objects.get(id=id)
    return render(request, "editarReparaciones.html", {"misreparaciones": reparacion})

def editarReparacion(request):
    id = request.POST["txtid"]
    fecha = request.POST["numfecha"]
    id_reloj = request.POST["numid_reloj"]
    descripcion_problema = request.POST["txtdescripcion_problema"]
    costo_de_reparacion = request.POST["numcosto_de_reparacion"]
    tiempo_de_reparacion = request.POST["txttiempo_de_reparacion"]
    estado_reparacion = request.POST["txtestado_reparacion"]
    reparacion = Reparacion.objects.get(id=id)
    reparacion.fecha = fecha
    reparacion.id_reloj = id_reloj
    reparacion.descripcion_problema = descripcion_problema
    reparacion.costo_de_reparacion = costo_de_reparacion
    reparacion.tiempo_de_reparacion = tiempo_de_reparacion
    reparacion.estado_reparacion = estado_reparacion

    reparacion.save()
    return redirect("reparaciones")

def borrarReparacion(request, id):
    reparacion = Reparacion.objects.get(id=id)
    reparacion.delete()
    return redirect("reparaciones")
