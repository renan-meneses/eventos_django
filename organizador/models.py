from django.db import models

# Create your models here.
class Organizador(models.Model):
	nome = models.CharField(max_length=255)
	sobrenome = models.CharField(max_length=255)
	email = models.EmailField()
	cnpj = models.CharField(max_length=14)

	def __str__ (self):
		return self.nome + self.sobrenome