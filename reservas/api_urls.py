from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from .api import Reservas

urlpatterns = [
    path('<str:ticket_code>', csrf_exempt(Reservas.as_view())),
]