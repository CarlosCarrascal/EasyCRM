from django.contrib import admin
from .models import Cliente, Producto, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_registro')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_registro',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)
    list_filter = ('precio',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'producto', 'cantidad', 'fecha', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__nombre', 'producto__nombre')
    date_hierarchy = 'fecha'
