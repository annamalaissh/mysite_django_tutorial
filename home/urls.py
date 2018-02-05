from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^xxx$', views.index, name='index'),
]