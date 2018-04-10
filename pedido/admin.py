# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['paciente' , 'medicacion',
                                         'medico'   , 'farmacia'  ,
                                         'dni'      , 'nro_afiliado'
                                         ]  }),
        ('Date information', {'fields': ['fecha'], 'classes': ['collapse']}),
    ]
    #inlines = [PedidoInline]
    list_display = ('paciente', 'medicacion', 'fecha')
    list_filter = ['fecha']
    search_fields = ['paciente']

admin.site.register(Pedido, PedidoAdmin)