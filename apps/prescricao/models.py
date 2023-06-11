from django.db import models
from medicamento.models import Medicamento

# Create your models here.

class Prescricao(models.Model):
    dosagem = models.CharField('Dosagem', max_length=50)
    medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.CASCADE)
    frequencia = models.CharField('Frequência', max_length=50)
    tratamento = models.CharField('Tratamento', max_length=100)

    class Meta:
        verbose_name = 'Prescrição'
        verbose_name_plural = 'Prescrições'
        ordering = ['id']

    def __str__(self):
        return f'Prescrição {self.id}'

