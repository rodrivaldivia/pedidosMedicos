# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Medico(models.Model):
    id = models.CharField(max_length = 200 , primary_key = True)
    @staticmethod
    def getMedico(id):
        try:
            medico = Medico.objects.get(pk=id)
        except Medico.DoesNotExist:
            medico = Medico(id = id)
        return medico

    def __str__(self):
        return self.id

