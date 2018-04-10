from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$' , views.redir_pedido , name='redir_pedido'),
    url(r'^nuevo/$', views.pedido, name='pedido'),
    url(r'^ver/(?P<id>[0-9]+)/$', views.ver_pedido , name='ver_pedido'),
    url(r'^update/(?P<id>[0-9]+)/$', views.update_pedido , name='update_pedido'),
    url(r'^listado/$', views.listado , name='listado'),

    url(r'^ajax/cargar-localidad/', views.load_localidades, name='ajax_load_localidades'),
    url(r'^ajax/cargar-paciente/', views.load_paciente , name='ajax_load_paciente'),
]