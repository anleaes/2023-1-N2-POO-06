from django.db import models

class Medicamento(models.Model):
    nome = models.CharField('Nome', max_length=100)
    numero_lote = models.IntegerField('Número do Lote')
    validade = models.DateField('Validade')
    
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['id']

    def __str__(self):
        return self.name