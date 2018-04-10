# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Medico
from pedido.models import Pedido
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def detail(request, medico_id):
    lista_pedidos = Pedido.objects.all()
    lista_pedidos = filter(lambda x: x.medico == medico_id, lista_pedidos)
    pedido = lista_pedidos[0] if lista_pedidos else None
    template = loader.get_template('iosfa/estadisticas/por_medico.html')
    context = {
        'lista_pedidos': lista_pedidos,
        'pedido': pedido,
    }
    return HttpResponse(template.render(context, request))
@login_required
def medico(request):
    lista_medicos = Medico.objects.order_by('id')
    template = loader.get_template('iosfa/medicos.html')
    context = {
        'lista_medicos': lista_medicos,
    }
    return HttpResponse(template.render(context, request))