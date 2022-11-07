from django.http import HttpResponse
from django.shortcuts import render
from django.template import  Template, Context,loader
from appfamiliar.models import Familiares

def greet(request):
 
    plantilla = loader.get_template("plantilla.html")

    message =""

    family = Familiares.objects.all()

    for miembro in family:
        message += f"Hola, soy {miembro.nombre}, {miembro.parentesco} de Israel. Tengo {miembro.edad}, mido {miembro.altura} y mi correo electronico es {miembro.email}," " | "

    
    datos = {"message": message}

    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

