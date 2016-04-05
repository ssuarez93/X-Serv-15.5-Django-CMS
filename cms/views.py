# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

# Create your views here.

def identificador(request, ident):
    try:
        pages = Pages.objects.get(id=int(ident))
        pagina = str(pages.page)
    except Pages.DoesNotExist:
        pagina = ("<h4>Error. No hay pagina para el identificador introducido</h3>")
    return HttpResponse(pagina)

def recurso(request, recurso):
    try:
        pages = Pages.objects.get(name=recurso)
        pagina = str(pages.page)
    except Pages.DoesNotExist:
        pagina = ("<h4>Error. No hay pagina para el recurso introducido</h3>")
    return HttpResponse(pagina)
