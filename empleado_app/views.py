from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.
def empleados(request):
    losempleados = Empleado.objects.all()
    return render(request, 'gestionarEmpleados.html', {"misempleados": losempleados})

def registrarEmpleado(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    cargo = request.POST["txtcargo"]
    telefono = request.POST["numtelefono"]
    correo = request.POST["txtcorreo"]
    anios_experiencia = request.POST["numanios_experiencia"]

    guardarEmpleado = Empleado.objects.create(
        id = id,
        nombre = nombre,
        apellido = apellido,
        cargo = cargo,
        telefono = telefono,
        correo = correo,
        anios_experiencia = anios_experiencia
    ) 
    return redirect("empleados")

def seleccionarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request, "editarEmpleados.html", {"misempleados": empleado})

def editarEmpleado(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    cargo = request.POST["txtcargo"]
    telefono = request.POST["numtelefono"]
    correo = request.POST["txtcorreo"]
    anios_experiencia = request.POST["numanios_experiencia"]
    empleado = Empleado.objects.get(id=id)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.cargo = cargo
    empleado.telefono = telefono
    empleado.correo = correo
    empleado.anios_experiencia = anios_experiencia

    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("empleados")
