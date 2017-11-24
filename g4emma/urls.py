from django.conf.urls import url
from g4emma import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^manual/$', views.manual, name='manual'),
    url(r'^simulation/$', views.simulation, name='simulation'),
    url(r'^tools/$', views.tools, name='tools'),
    url(r'^results/$', views.results, name='results'),
    url(r'^progress/$', views.progress, name='progress'),
]
