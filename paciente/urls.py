from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.paciente , name='paciente'),
    url(r'^(?P<paciente_id>[\w|\W]+)/$', views.detail, name='detail'),
]