from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, PedidoForm

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'CRMapp/clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'CRMapp/clientes/cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'CRMapp/clientes/cliente_form.html'
    success_url = reverse_lazy('cliente-list')
    success_message = "Cliente creado exitosamente"

class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'CRMapp/clientes/cliente_form.html'
    success_url = reverse_lazy('cliente-list')
    success_message = "Cliente actualizado exitosamente"

class ClienteDeleteView(SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'CRMapp/clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')
    success_message = "Cliente eliminado exitosamente"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'CRMapp/productos/producto_list.html'
    context_object_name = 'productos'
    paginate_by = 10

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'CRMapp/productos/producto_detail.html'
    context_object_name = 'producto'

class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'CRMapp/productos/producto_form.html'
    success_url = reverse_lazy('producto-list')
    success_message = "Producto creado exitosamente"

class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'CRMapp/productos/producto_form.html'
    success_url = reverse_lazy('producto-list')
    success_message = "Producto actualizado exitosamente"

class ProductoDeleteView(SuccessMessageMixin, DeleteView):
    model = Producto
    template_name = 'CRMapp/productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')
    success_message = "Producto eliminado exitosamente"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Vistas para Pedido
class PedidoListView(ListView):
    model = Pedido
    template_name = 'CRMapp/pedidos/pedido_list.html'
    context_object_name = 'pedidos'
    paginate_by = 10

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'CRMapp/pedidos/pedido_detail.html'
    context_object_name = 'pedido'

class PedidoCreateView(SuccessMessageMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'CRMapp/pedidos/pedido_form.html'
    success_url = reverse_lazy('pedido-list')
    success_message = "Pedido creado exitosamente"

class PedidoUpdateView(SuccessMessageMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'CRMapp/pedidos/pedido_form.html'
    success_url = reverse_lazy('pedido-list')
    success_message = "Pedido actualizado exitosamente"

class PedidoDeleteView(SuccessMessageMixin, DeleteView):
    model = Pedido
    template_name = 'CRMapp/pedidos/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido-list')
    success_message = "Pedido eliminado exitosamente"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

# Vista para la página de inicio
def home(request):
    total_clientes = Cliente.objects.count()
    total_productos = Producto.objects.count()
    total_pedidos = Pedido.objects.count()
    pedidos_recientes = Pedido.objects.order_by('-fecha')[:5]
    
    context = {
        'total_clientes': total_clientes,
        'total_productos': total_productos,
        'total_pedidos': total_pedidos,
        'pedidos_recientes': pedidos_recientes,
    }
    
    return render(request, 'CRMapp/home.html', context)
