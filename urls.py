from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Proyectos, name='proyectos'),
    url(r'^(?P<proyecto_id>[0-9]+)/$', views.Detail, name='detail'),
    url(r'^(?P<proyecto_id>[0-9]+)/del$', views.DeleteProyecto, name='delete'),
    url(r'^(?P<proyecto_id>[0-9]+)/getcsv$', views.getCsv, name='csv'),
    url(r'^(?P<proyecto_id>[0-9]+)/m=(?P<m_id>[0-9]+)$', views.inscribir_curso,name='inscribir'),
    url(r'^add/$', views.AddProyecto,name='add'),
]