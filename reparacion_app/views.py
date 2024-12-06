from django.shortcuts import render, redirect
from .models import Reparacion
# Create your views here.
def reparaciones(request):
    lasreparaciones = Reparacion.objects.all()
    return render(request, 'gestionarReparaciones.html', {"misreparaciones": lasreparaciones})

def registrarReparacion(request):
    idreparacion = request.POST["txtid"]
    fecha_recepcion = request.POST["numfecha"]
    id_reloj = request.POST["numid_reloj"]
    descripcion_problema = request.POST["txtdescripcion_problema"]
    costo_de_reparacion = request.POST["numcosto_de_reparacion"]
    tiempo_de_reparacion = request.POST["txttiempo_de_reparacion"]
    estado_reparacion = request.POST["txtestado_reparacion"]
    detalles=request.POST["txtdetalles"]
    id_empleado=request.POST["txtide"]
    id_cliente=request.POST["txtidc"]
    fecha_entrega=request.POST["datef"]

    guardarReparacion = Reparacion.objects.create(
        idreparacion = idreparacion,
        fecha_recepcion = fecha_recepcion,
        id_reloj = id_reloj,
        descripcion_problema = descripcion_problema,
        costo_de_reparacion = costo_de_reparacion,
        tiempo_de_reparacion = tiempo_de_reparacion,
        estado_reparacion = estado_reparacion,
        detalles=detalles,
        id_empleado=id_empleado,
        id_cliente=id_cliente,
        fecha_entrega=fecha_entrega
    ) 
    return redirect("reparaciones")

def seleccionarReparacion(request, idreparacion):
    reparacion = Reparacion.objects.get(idreparacion=idreparacion)
    return render(request, "editarReparaciones.html", {"misreparaciones": reparacion})

def editarReparacion(request):
    idreparacion = request.POST["txtid"]
    fecha_recepcion = request.POST["numfecha"]
    id_reloj = request.POST["numid_reloj"]
    descripcion_problema = request.POST["txtdescripcion_problema"]
    costo_de_reparacion = request.POST["numcosto_de_reparacion"]
    tiempo_de_reparacion = request.POST["txttiempo_de_reparacion"]
    estado_reparacion = request.POST["txtestado_reparacion"]
    detalles=request.POST["txtdetalles"]
    id_empleado=request.POST["txtide"]
    id_cliente=request.POST["txtidc"]
    fecha_entrega=request.POST["datef"]
    reparacion = Reparacion.objects.get(idreparacion=idreparacion)
    reparacion.fecha_recepcion = fecha_recepcion
    reparacion.id_reloj = id_reloj
    reparacion.descripcion_problema = descripcion_problema
    reparacion.costo_de_reparacion = costo_de_reparacion
    reparacion.tiempo_de_reparacion = tiempo_de_reparacion
    reparacion.estado_reparacion = estado_reparacion
    reparacion.detalles=detalles
    reparacion.id_empleado=id_empleado
    reparacion.id_cliente=id_cliente
    reparacion.fecha_entrega=fecha_entrega


    reparacion.save()
    return redirect("reparaciones")

def borrarReparacion(request, idreparacion):
    reparacion = Reparacion.objects.get(idreparacion=idreparacion)
    reparacion.delete()
    return redirect("reparaciones")
