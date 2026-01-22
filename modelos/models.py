from django.db import models
import uuid


def generar_code():
    return uuid.uuid4().hex


class Modelo(models.Model):
    SEGMENTOS = (
        ("VANS", "Utilitario"),
        ("CAMIONES", "Pesados"),
        ("BUSES", "Colectivos"),
    )
    nombre = models.CharField(max_length=50)
    tipo_de_modelo = models.CharField(max_length=50)
    fecha_de_inicio = models.DateField(auto_now_add=True)
    segmentos = models.CharField(choices=SEGMENTOS, max_length=50)
    code = models.CharField(
        max_length=32,
        unique=True,
        default=generar_code
    )

    def __str__(self):
        return f"Nombre: {self.nombre} - Segmentos: {self.segmentos}"


