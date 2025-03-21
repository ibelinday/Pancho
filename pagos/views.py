from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def index(request):
    plantilla = loader.get_template("index.html")
    contexto = {}

    return HttpResponse(plantilla.render(contexto,request))

