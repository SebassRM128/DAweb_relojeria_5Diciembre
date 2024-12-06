from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def clientes(request):
    losclientes = Cliente.objects.all()
    return render(request, 'gestionarClientes.html', {"misclientes": losclientes})

def registrarCliente(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    correo_electronico = request.POST["txtcorreo_electronico"]
    fecha_de_nacimiento = request.POST["numfecha_nacimiento"]

    guardarCliente = Cliente.objects.create(
        id = id,
        nombre = nombre,
        apellido = apellido,
        direccion = direccion,
        telefono = telefono,
        correo_electronico = correo_electronico,
        fecha_de_nacimiento = fecha_de_nacimiento
    ) 
    return redirect("clientes")

def seleccionarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "editarClientes.html", {"misclientes": cliente})

def editarCliente(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["numtelefono"]
    correo_electronico = request.POST["txtcorreo_electronico"]
    fecha_de_nacimiento = request.POST["numfecha_nacimiento"]
    cliente = Cliente.objects.get(id=id)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.correo_electronico = correo_electronico
    cliente.fecha_de_nacimiento = fecha_de_nacimiento

    cliente.save()
    return redirect("clientes")

def borrarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("clientes")
