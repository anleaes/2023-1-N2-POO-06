from django.db import models

# Create your models here.

class Paciente(models.Model):
    name = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    data_nascimento = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=100)
    historico = models.CharField('Histórico', max_length=100)
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outroa'),
    )
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['id']

    def __str__(self):
        return self.name


