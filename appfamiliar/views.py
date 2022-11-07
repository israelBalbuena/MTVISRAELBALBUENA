from django.http import HttpResponse
from django.shortcuts import render
from django.template import  Template, Context,loader
from appfamiliar.models import Familiares

def greet(request):
 
    plantilla = loader.get_template("plantilla.html")

    message =[]

    family = Familiares.objects.all()

    for miembro in family:
        message.append( f"Hola, soy {miembro.nombre}, {miembro.parentesco} de Israel. Nací en {miembro.fecha_nacimiento} y tengo {miembro.edad} años, mido {miembro.altura} centimetros y mi correo electronico es {miembro.email}")
  
    datos = {"message": message}

    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

