from django.db import models
from paciente.models import Paciente

# Create your models here.


class Medico(models.Model):
    nome = models.CharField('Nome', max_length=50)
    especialidade = models.CharField('Especialidade', max_length=50)
    paciente = models.ForeignKey(
        Paciente, verbose_name='Paciente', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        ordering = ['id']

    def __str__(self):
        return self
