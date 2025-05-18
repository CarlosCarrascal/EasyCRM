from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Cliente URLs
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
    
    # Producto URLs
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('productos/nuevo/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto-delete'),
    
    # Pedido URLs
    path('pedidos/', views.PedidoListView.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido-detail'),
    path('pedidos/nuevo/', views.PedidoCreateView.as_view(), name='pedido-create'),
    path('pedidos/<int:pk>/editar/', views.PedidoUpdateView.as_view(), name='pedido-update'),
    path('pedidos/<int:pk>/eliminar/', views.PedidoDeleteView.as_view(), name='pedido-delete'),
]