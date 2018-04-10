# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from paciente.models import Paciente
from medico.models import Medico
from .models import Pedido, Localidad, Provincia
import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import PedidosForm , EstadoForm

@login_required
def pedido(request):
    pedido_inst = Pedido()

    form = PedidosForm()
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = PedidosForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            pedido_inst.fecha = form.cleaned_data['pedido_date']

            pedido_inst.medicacion = form.cleaned_data['pedido_medicacion']
            pedido_inst.forma_farmaceutica = form.cleaned_data['pedido_forma_farmaceutica']
            pedido_inst.dosis = form.cleaned_data['pedido_dosis']

            pedido_inst.paciente = form.cleaned_data['pedido_paciente']
            pedido_inst.dni = form.cleaned_data['pedido_dni']
            pedido_inst.nro_afiliado = form.cleaned_data['pedido_nro_afiliado']
            pedido_inst.provincia = form.cleaned_data['pedido_provincia']
            pedido_inst.localidad = form.cleaned_data['pedido_localidad']
            pedido_inst.direccion = form.cleaned_data['pedido_direccion']
            pedido_inst.telefono = form.cleaned_data['pedido_telefono']

            pedido_inst.medico = form.cleaned_data['pedido_medico']
            pedido_inst.farmacia = form.cleaned_data['pedido_farmacia']


            pedido_inst.save()

            #TODO agregar lo que haga falta
            new_paciente = Paciente.getPaciente(pedido_inst.paciente)
            new_paciente.id = pedido_inst.paciente
            new_paciente.dni = pedido_inst.dni
            new_paciente.nro_afiliado = pedido_inst.nro_afiliado
            new_paciente.save()

            new_medico = Medico.getMedico(pedido_inst.medico)
            new_medico.id = pedido_inst.medico
            new_medico.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('home') )

    # If this is a GET (or any other method) create the default form.

    return render(request, 'iosfa/pedido.html', {'form': form, 'pedido_inst':pedido_inst})
    #return HttpResponseRedirect(reverse('login') )

@login_required
def redir_pedido(request):
    return HttpResponseRedirect( reverse('pedido'))

@login_required
def update_pedido(request , id):

    lista_pedidos = Pedido.objects.all()
    pedido = next((x for x in lista_pedidos if x.id == int(id)), None)

    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            pedido.estado = form.cleaned_data['pedido_estado']
            pedido.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = EstadoForm()
    template = loader.get_template('iosfa/update_pedido.html')
    context = {
        'pedido': pedido ,
        'form' : form
    }
    return HttpResponse(template.render(context, request))

@login_required
def ver_pedido(request , id):

    lista_pedidos = Pedido.objects.all()
    pedido = next((x for x in lista_pedidos if x.id == int(id)), None)

    template = loader.get_template('iosfa/ver_pedido.html')
    context = {
        'pedido': pedido
    }
    return HttpResponse(template.render(context, request))

@login_required
def listado(request):
    lista_pedidos = Pedido.objects.all()

    pedido = lista_pedidos[0] if lista_pedidos else None

    template = loader.get_template('iosfa/lista_pedidos.html')
    context = {
        'lista_pedidos': lista_pedidos,
        'pedido': pedido ,
    }

    return HttpResponse(template.render(context, request))

def new_pedido(fecha, paciente, afiliado, dni, medicacion,
               forma,   dosis,  medico, farmacia, direccion):

    pedido_inst = Pedido()
    pedido_inst.fecha = fecha
    pedido_inst.medicacion = medicacion
    pedido_inst.paciente = paciente
    pedido_inst.medico = medico
    pedido_inst.nro_afiliado = afiliado
    pedido_inst.telefono = 48923548
    pedido_inst.forma_farmaceutica = forma
    pedido_inst.farmacia = farmacia
    pedido_inst.direccion = direccion
    pedido_inst.dni = dni
    pedido_inst.dosis = dosis
    pedido_inst.provincia = Provincia.objects.get(name='Capital Federal')
    pedido_inst.localidad = Localidad.objects.get(name='Ciudad Autonoma Buenos Aires')

    pedido_inst.save()

    new_paciente = Paciente.getPaciente(pedido_inst.paciente)
    new_paciente.id = pedido_inst.paciente
    new_paciente.nro_afiliado = pedido_inst.nro_afiliado
    new_paciente.dni = pedido_inst.dni
    new_paciente.save()

    new_medico = Medico.getMedico(pedido_inst.medico)
    new_medico.id = pedido_inst.medico
    new_medico.save()

def load_localidades(request):
    provincia_id = request.GET.get('provincia')
    print provincia_id
    localidades = Localidad.objects.filter(provincia_id=provincia_id).order_by('name')
    #print localidades
    return render(request, 'iosfa/opciones_localidades.html', {'localidades': localidades})

def load_paciente(request):
    nro_afiliado = request.GET.get('nro_afiliado')
    pedidos = Pedido.objects.filter(nro_afiliado=nro_afiliado).order_by('paciente')
    if pedidos.first():
        p = pedidos.first()
        data = {
            'nombre': p.paciente,
            'dni': p.dni,
            'direccion': p.direccion ,
            'telefono': p.telefono ,
            'provincia': p.provincia.id ,
            'localidad': p.localidad.id ,
        }
        return JsonResponse(data)
    else:
        print 'No hay paciente con ese ID'

    #return render(request, 'iosfa/opciones_localidades.html', {'localidades': localidades})

def delete_medicos():
    for m in Medico.objects.all():
        m.delete()

def delete_pacientes():
    for p in Paciente.objects.all():
        p.delete()

def delete_pedidos():
    for p in Pedido.objects.all():
        p.delete()

def delete_db():
    delete_medicos()
    delete_pacientes()
    delete_pedidos()
