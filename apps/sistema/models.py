from django.db import models
from paciente.models import Paciente
from medico.models import Medico
from prontuario.models import Prontuario


class Sistema(models.Model):
    paciente = models.ForeignKey(
        Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    medico = models.ForeignKey(
        Medico, verbose_name='Medico', on_delete=models.CASCADE)
    prontuario = models.ForeignKey(
        Prontuario, verbose_name='Prontuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['id']

    def str(self):
        return f"Paciente: {self.paciente.name}"
