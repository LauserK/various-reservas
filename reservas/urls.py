from django.urls import path
from .views import TicketView, CreateTicket

urlpatterns = [
    path('ticket/<str:ticket_code>/', TicketView.as_view(), name='ticket-view'),
    path('ticket/', CreateTicket.as_view()),
]