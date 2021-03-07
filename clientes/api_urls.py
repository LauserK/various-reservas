from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from .api import Clientes

urlpatterns = [
    path('create', csrf_exempt(Clientes.as_view())),
]