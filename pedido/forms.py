# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Select
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Provincia, Localidad
import datetime , string #for checking renewal date range.

class PedidosForm(forms.Form):

    pedido_paciente = forms.CharField(help_text="Ingresar nombre del paciente" , label="Paciente")
    pedido_dni = forms.IntegerField(help_text="Ingresar DNI del paciente" , label="DNI")
    pedido_nro_afiliado = forms.IntegerField(help_text="Ingresar numero de afiliado del paciente"
                                             , label="Numero de Afiliado")
    pedido_direccion = forms.CharField(help_text="Ingresar direccion del paciente"
                                       , label="Dirección")

    pedido_localidad = forms.ModelChoiceField(queryset=Localidad.objects.all(), label="Localidad")
    #pedido_provincia = forms.CharField(help_text="Ingresar provincia" , label="Provincia" , widget=Select)
    pedido_provincia = forms.ModelChoiceField(queryset=Provincia.objects.all(), label="Provincia")

    pedido_telefono = forms.CharField(help_text="Ingresar telefono del paciente" , label="Telefono")

    pedido_date = forms.DateField(help_text="Ingresar fecha de pedido" , widget=SelectDateWidget
                                  , label="Fecha")

    pedido_medico = forms.CharField(help_text="Ingresar medico" , label="Medico")
    pedido_farmacia = forms.CharField(help_text="Ingresar farmacia" , label="Farmacia")

    pedido_medicacion = forms.CharField(help_text="Ingresar medicacion" , label="Medicación")
    pedido_forma_farmaceutica = forms.CharField(help_text="Ingresar forma farmaceutica" ,
                                                label="Forma farmaceutica")
    pedido_dosis = forms.CharField(help_text="Ingresar dosis" , label="Dosis")


    def __init__(self, *args, **kwargs):
        super(forms.Form,self).__init__(*args, **kwargs)
        self.fields['pedido_localidad'].queryset = Localidad.objects.none()

        if 'pedido_provincia' in self.data:
            try:
                provincia_id = self.data.get('pedido_provincia')
                self.fields['pedido_localidad'].queryset = Localidad.objects.filter(provincia_id=provincia_id).order_by('name')
                print self.fields['pedido_localidad'].queryset
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        #else:
         #   self.fields['pedido_localidad'].queryset = self.pedido_provincia.localidad_set.order_by('name')


    def clean_pedido_date(self):
        data = self.cleaned_data['pedido_date']

        #Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Fecha Invalida'))

        # Remember to always return the cleaned data.
        return data

class EstadoForm(forms.Form):
    opciones = (
        ('EM', 'Emitido'),
        ('TR', 'En Transito'),
        ('FI', 'Firmado'),
        ('PR', 'Presentado'),
        ('PA', 'Pago'),
    )
    pedido_estado = forms.MultipleChoiceField(  choices = opciones,
                                                label="Estado")

    def clean_pedido_estado(self):
        data = self.cleaned_data['pedido_estado']

        data = data[0]
        # Remember to always return the cleaned data.
        return data