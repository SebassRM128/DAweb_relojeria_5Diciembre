from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.
def ventas(request):
    lasventas = Venta.objects.all()
    return render(request, 'gestionarVentas.html', {"misventas": lasventas})

def registrarVenta(request):
    id = request.POST["txtid"]
    fecha = request.POST["numfecha"]
    id_reloj = request.POST["numid_reloj"]
    id_cliente = request.POST["numid_cliente"]

    precio_de_venta = request.POST["numprecio_de_venta"]
    cantidad = request.POST["txtcantidad"]
    estado_de_entrega = request.POST["txtestado_de_entrega"]
    id_empleado=request.POST["numide"]

    guardarVenta = Venta.objects.create(
        id = id,
        fecha = fecha,
        id_reloj = id_reloj,
        id_cliente = id_cliente,
        precio_de_venta = precio_de_venta,
        cantidad = cantidad,
        estado_de_entrega = estado_de_entrega,
        id_empleado=id_empleado
    ) 
    return redirect("ventas")

def seleccionarVenta(request, id):
    venta = Venta.objects.get(id=id)
    return render(request, "editarVentas.html", {"misventas": venta})

def editarVenta(request):
    id = request.POST["txtid"]
    fecha = request.POST["numfecha"]
    id_reloj = request.POST["numid_reloj"]
    id_cliente = request.POST["numid_cliente"]
    precio_de_venta = request.POST["numprecio_de_venta"]
    cantidad = request.POST["txtcantidad"]
    estado_de_entrega = request.POST["txtestado_de_entrega"]
    id_empleado=request.POST["numide"]
    venta = Venta.objects.get(id=id)
    venta.fecha = fecha
    venta.id_reloj = id_reloj
    venta.id_cliente = id_cliente
    venta.precio_de_venta = precio_de_venta
    venta.cantidad = cantidad
    venta.id_empleado=id_empleado
    venta.estado_de_entrega = estado_de_entrega

    venta.save()
    return redirect("ventas")

def borrarVenta(request, id):
    venta = Venta.objects.get(id=id)
    venta.delete()
    return redirect("ventas")
