from django.db import models

class Farmacia(models.Model):
    estoque = models.CharField('estoque', max_length=50)
    medicamento = models.CharField('medicamento', max_length=50)
    lotes = models.CharField('lotes', max_length=50)

    class Meta:
        verbose_name = 'Farmacia'
        verbose_name_plural = 'Farmacias'
        ordering = ['id']

    def __str__(self):
        return self.medicamento

