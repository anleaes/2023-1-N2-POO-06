from django.db import models
from paciente.models import Paciente


class Prontuario(models.Model):
    paciente = models.ForeignKey(
        Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    data_criacao = models.DateField('Data de Criação')
    sintomas = models.CharField('Sintomas', max_length=100)
    diagnostico = models.CharField('Diagnóstico', max_length=100)

    class Meta:
        verbose_name = 'Prontuario'
        verbose_name_plural = 'Prontuarios'
        ordering = ['id']

    def __str__(self):
        return self.diagnostico
