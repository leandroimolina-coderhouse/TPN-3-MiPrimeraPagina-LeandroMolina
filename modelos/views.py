from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from modelos.models import Modelo
from django.contrib.auth.mixins import LoginRequiredMixin


class ModeloListView(LoginRequiredMixin, ListView):
    model = Modelo
    template_name = "modelos/modelo_list.html"
    context_object_name = "modelos"
    
class ModeloDetailView(LoginRequiredMixin, DetailView):
    model = Modelo
    template_name = "modelos/modelo_detail.html"
    context_object_name = "modelo"
    slug_field = "code"
    slug_url_kwarg = "code"

class ModeloCreateView(LoginRequiredMixin, CreateView):
    model = Modelo
    fields = ["nombre", "tipo_de_modelo", "segmentos"]
    # form_class = MedicoForm
    template_name = "modelos/modelo_form.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "modelo_detail",
            kwargs={"code": self.object.code}
        )


class ModeloUpdateView(LoginRequiredMixin, UpdateView):
    model = Modelo
    fields = ["nombre", "tipo_de_modelo"]
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_success_url(self):
        return reverse_lazy(
            "modelo_detail",
            kwargs={"code": self.object.code}
        )


class ModeloDeleteView(LoginRequiredMixin, DeleteView):
    model = Modelo
    template_name = "modelos/modelo_confirm_delete.html"
    success_url = reverse_lazy("modelo_list")