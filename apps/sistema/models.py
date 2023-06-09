from django.db import models

class Sistema(models.Model):
    paciente = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    prontuario = models.TextField()

    def __str__(self):
        return self.paciente
