# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DadosPessoais(models.Model):
	name= models.CharField(max_length=100, verbose_name='Nome')
	city = models.CharField(max_length=100, verbose_name='Cidade')
	cpf = models.CharField(max_length=12, verbose_name='CPF')
	email = models.EmailField(verbose_name='Email')

	def __str__(self):
		return self .name

	class Meta:
		verbose_name = 'Dados Pessoais'
		verbose_name_plural = 'Dados Pessoais'