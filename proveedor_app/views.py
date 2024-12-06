from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.
def proveedores(request):
    losproveedores = Proveedor.objects.all()
    return render(request, 'gestionarProveedores.html', {"misproveedores": losproveedores})

def registrarProveedor(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    correo = request.POST["txtcorreo"]
    numero_de_cuenta = request.POST["numcuenta"]
    pais_de_origen = request.POST["txtpais_de_origen"]

    guardarProveedor = Proveedor.objects.create(
        id = id,
        nombre = nombre,
        direccion = direccion,
        telefono = telefono,
        correo = correo,
        numero_de_cuenta = numero_de_cuenta,
        pais_de_origen = pais_de_origen
    ) 
    return redirect("proveedores")

def seleccionarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    return render(request, "editarProveedores.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    correo = request.POST["txtcorreo"]
    numero_de_cuenta = request.POST["numcuenta"]
    pais_de_origen = request.POST["txtpais_de_origen"]
    proveedor = Proveedor.objects.get(id=id)
    proveedor.nombre = nombre
    proveedor.direccion = direccion
    proveedor.telefono = telefono
    proveedor.correo = correo
    proveedor.numero_de_cuenta = numero_de_cuenta
    proveedor.pais_de_origen = pais_de_origen

    proveedor.save()
    return redirect("proveedores")

def borrarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect("proveedores")
