from django.test import TestCase
from .models import Sistema

class SistemaTestCase(TestCase):
    def setUp(self):
        self.sistema = Sistema(paciente="João", medico="Dr. Silva", prontuario="Lorem ipsum dolor sit amet")

    def test_paciente(self):
        self.assertEqual(self.sistema.paciente, "João")

    def test_medico(self):
        self.assertEqual(self.sistema.medico, "Dr. Silva")

    def test_prontuario(self):
        self.assertEqual(self.sistema.prontuario, "Lorem ipsum dolor sit amet")
