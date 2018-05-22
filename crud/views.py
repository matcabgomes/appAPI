# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import DadosPessoais


# tem object.filter para filtrar a busca no banco
def crud_exibir(request):

    pessoas = DadosPessoais.objects.all()
    context = {'pessoas': pessoas}
    return render(request, 'crud/crud_exibir.html', context)
