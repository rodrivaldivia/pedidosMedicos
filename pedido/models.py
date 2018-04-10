# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator

class PhoneModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefono en el formato: '+999999999'. Hasta 15 digitos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

class Provincia(models.Model):
    name = models.CharField(max_length=50, default='Capital Federal')

    def __str__(self):
        return self.name

class Localidad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Ciudad Autonoma de Buenos Aires')

    def __str__(self):
        return self.name

@python_2_unicode_compatible  # only if you need to support Python 2
class Pedido(models.Model):
    """
    Model representing a pedido
    """
    medico = models.CharField(max_length=200, default='')
    farmacia = models.CharField(max_length=200, default='-')

    paciente = models.CharField(max_length=200, default='' )
    dni = models.PositiveIntegerField( default = 1)
    nro_afiliado = models.PositiveIntegerField( default = 1)
    direccion = models.CharField(max_length=200, default='-')
    telefono = models.CharField(max_length=17, blank=True, default='-')
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True, default=Localidad(provincia=Provincia()))
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, default=Provincia())


    medicacion = models.CharField(max_length=200, default='')
    forma_farmaceutica = models.CharField(max_length=200, default='-')
    dosis = models.CharField(max_length=200, default='-')

    fecha = models.DateField(null=True, blank=True)
    opciones = (
        ('EM', 'Emitido'),
        ('TR', 'En Transito'),
        ('FI', 'Firmado'),
        ('PR', 'Presentado'),
        ('PA', 'Pago'),
    )
    estado = models.CharField(max_length=2, choices=opciones, blank=True, default='EM', help_text='Estado del pedido')

    class Meta:
        permissions = (("can_create","Puede hacer pedidos"),
                       ("can_edit","Puede editar el estado"))


    def display_telefono(self):
        return self.telefono

    def display_dni(self):
        import string
        return string.replace("{:,}".format(self.dni) , "," , ".")

    def update_estado(self, estado):
        self.estado = estado
        self.save()

    def __str__(self):
        return self.paciente + ' - ' + self.medicacion
