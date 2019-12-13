from django.db import models

# Create your models here.
class Participante(models.Model):
	nome_participante = models.CharField(max_length=255)
	email = models.EmailField()
	cpf = models.CharField(max_length=11)

	def __str__ (self):
		return self.nome