from django.db import models
from paciente.models import Paciente
# from prescricao.models import Prescricao

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE)
    data_criacao = models.DateField('Data de Criação')
    sintomas = models.CharField('Frequência', max_length=100)
    diagnostico = models.CharField('Tratamento', max_length=100)
    # prescicao = models.ForeignKey(Prescricao, verbose_name='Prescricao', on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Prontuario'
        verbose_name_plural = 'Prontuarios'
        ordering = ['id']

    def __str__(self):
        return self.diagnostico