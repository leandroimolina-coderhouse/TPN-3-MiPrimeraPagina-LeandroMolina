from django.urls import path
from .views import (
    ModeloListView,
    ModeloDetailView,
    ModeloCreateView,
    ModeloUpdateView,
    ModeloDeleteView,
)

urlpatterns = [
    path('', ModeloListView.as_view(), name='modelo_list'),
    path('crear/', ModeloCreateView.as_view(), name='modelo_create'),
    path('<slug:code>/', ModeloDetailView.as_view(), name='modelo_detail'),
    path('<slug:code>/editar/', ModeloUpdateView.as_view(), name='modelo_update'),
    path('<slug:code>/eliminar/', ModeloDeleteView.as_view(), name='modelo_delete'),
]
