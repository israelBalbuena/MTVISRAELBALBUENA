from django.http import HttpResponse
from django.shortcuts import render
from django.template import  Template, Context,loader
from appfamiliar.models import Familiares

def greet(request):

    mama = Familiares(1,"madre","Francisca","Balbuena", 61, "1961-12-03",1.65,"francisbal@live.com.mx")
    
    mama.save()
 
    datos = {"nombre": mama.nombre, "parentesco": mama.parentesco,"fecha_nacimiento":mama.fecha_nacimiento}

    plantilla = loader.get_template("plantilla.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)

