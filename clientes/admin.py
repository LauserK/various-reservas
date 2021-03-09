from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('correo','nombre')
    list_display = ('nombre','ci','estado','verificado')
    list_filter = ('verificado','estado','host')