from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.medico , name='medico'),
    url(r'^(?P<medico_id>[\w|\W]+)/$', views.detail, name='detail'),
]