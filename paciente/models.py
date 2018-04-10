# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Paciente(models.Model):
    id = models.CharField(max_length=200 , primary_key=True)
    dni = models.PositiveIntegerField( default = 1)
    nro_afiliado = models.PositiveIntegerField( default = 1)
    @staticmethod
    def getPaciente(id):
        try:
            paciente = Paciente.objects.get(pk=id)
        except Paciente.DoesNotExist:
            paciente = Paciente(id = id)

        return paciente

    def __str__(self):
        return self.id


    def display_dni(self):
        import string
        return string.replace("{:,}".format(self.dni) , "," , ".")


    def display_afiliado(self):
        import string
        return string.replace("{:,}".format(self.nro_afiliado) , "," , ".")