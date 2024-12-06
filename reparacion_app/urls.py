from django.urls import path
from reparacion_app import views

urlpatterns = [
    path("reparaciones",views.reparaciones,name="reparaciones"),
    path("registrarReparacion/",views.registrarReparacion,name="registrarReparacion"),
    path("seleccionarReparacion/<idreparacion>",views.seleccionarReparacion,name="seleccionarReparacion"),
    path("editarReparacion/",views.editarReparacion, name="editarReparacion"),
    path("borrarReparacion/<idreparacion>",views.borrarReparacion,name="borrarReparacion"),
    
]