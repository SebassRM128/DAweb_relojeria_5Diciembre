from django.urls import path
from reloj_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path("relojes",views.relojes,name="relojes"),
    path("registrarReloj/",views.registrarReloj,name="registrarReloj"),
    path("seleccionarReloj/<id>",views.seleccionarReloj,name="seleccionarReloj"),
    path("editarReloj/",views.editarReloj, name="editarReloj"),
    path("borrarReloj/<id>",views.borrarReloj,name="borrarReloj"),
    
]