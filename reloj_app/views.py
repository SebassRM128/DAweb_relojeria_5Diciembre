from django.shortcuts import render, redirect
from .models import Reloj
# Create your views here.
def index(request):
    return render(request, 'index.html')

def relojes(request):
    losrelojes = Reloj.objects.all()
    return render(request, 'gestionarRelojes.html', {"misrelojes": losrelojes})

def registrarReloj(request):
    id = request.POST["txtid"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    material = request.POST["txtmaterial"]
    precio = request.POST["numprecio"]
    anio_de_lanzamiento = request.POST["numaño"]
    idproveedor=request.POST["numidp"]

    guardarReloj = Reloj.objects.create(
        id = id,
        marca = marca,
        modelo = modelo,
        material = material,
        precio = precio,
        anio_de_lanzamiento = anio_de_lanzamiento,
        idproveedor=idproveedor
    ) 
    return redirect("relojes")

def seleccionarReloj(request, id):
    reloj = Reloj.objects.get(id=id)
    return render(request, "editarRelojes.html", {"misrelojes": reloj})

def editarReloj(request):
    id = request.POST["txtid"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    material = request.POST["txtmaterial"]
    precio = request.POST["numprecio"]
    anio_de_lanzamiento = request.POST["numaño"]
    idproveedor=request.POST["numidp"]
    reloj = Reloj.objects.get(id=id)
    reloj.marca = marca
    reloj.modelo = modelo
    reloj.material = material
    reloj.precio = precio
    reloj.anio_de_lanzamiento = anio_de_lanzamiento
    reloj.idproveedor = idproveedor

    reloj.save()
    return redirect("relojes")

def borrarReloj(request, id):
    reloj = Reloj.objects.get(id=id)
    reloj.delete()
    return redirect("relojes")
