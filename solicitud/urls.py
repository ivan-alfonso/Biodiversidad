from django.conf.urls import url
from solicitud import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]