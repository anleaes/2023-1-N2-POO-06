from django.db import models
from medicamento.models import Medicamento

class Prescricao(models.Model):
    medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.CASCADE)
    dosagem = models.CharField('Dosagem')
    frequencia = models.CharField('Frequência')
    tratamento = models.CharField('Tratamento')
    
    class Meta:
        verbose_name = 'Prontuario'
        verbose_name_plural = 'Prontuarios'
        ordering = ['id']

    def __str__(self):
        return self.name