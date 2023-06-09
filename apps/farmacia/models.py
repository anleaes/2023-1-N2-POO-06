from django.db import models

class Farmacia(models.Model):
    estoque = models.CharField('Estoque', max_length=50)
    medicamento = models.CharField('Medicamento', max_length=50)
    lotes = models.CharField('Lotes', max_length=50)

    class Meta:
        verbose_name = 'Farmácia'
        verbose_name_plural = 'Farmácias'
        ordering = ['id']

    def __str__(self):
        return self.medicamento
