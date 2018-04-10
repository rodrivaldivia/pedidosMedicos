# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
from pedido.models import Pedido
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def detail(request, paciente_id):
    lista_pedidos = Pedido.objects.all()
    print lista_pedidos
    lista_pedidos = filter(lambda x: x.paciente == paciente_id, lista_pedidos)
    #TODO agregar cantidad de pedidos arriba y esas cosas
    #TODO ordenar por fecha y eso (y también en medico)

    pedido = lista_pedidos[0] if lista_pedidos else None

    template = loader.get_template('iosfa/estadisticas/por_paciente.html')
    context = {
        'lista_pedidos': lista_pedidos,

        'pedido': pedido ,
    }

    return HttpResponse(template.render(context, request))

@login_required
def paciente(request):
    lista_pacientes = Paciente.objects.order_by('id')
    template = loader.get_template('iosfa/paciente.html')
    context = {
        'lista_pacientes': lista_pacientes,
    }
    return HttpResponse(template.render(context, request))