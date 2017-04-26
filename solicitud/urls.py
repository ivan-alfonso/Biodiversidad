from django.conf.urls import url
from solicitud.views import index

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]