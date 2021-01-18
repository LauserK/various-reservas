from django.urls import path
from .views import TicketView

urlpatterns = [
    path('ticket/<str:ticket_code>/', TicketView.as_view(), name='ticket-view'),
]