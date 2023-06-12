from django.db import models
from medicamento.models import Medicamento

class Farmacia(models.Model):
    estoque = models.CharField('estoque', max_length=50)
    medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.CASCADE)
    lotes = models.CharField('lotes', max_length=50)

    class Meta:
        verbose_name = 'Farmacia'
        verbose_name_plural = 'Farmacias'
        ordering = ['id']

    def __str__(self):
        return self.medicamento

