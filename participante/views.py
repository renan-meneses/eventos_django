from django.shortcuts import render
from django.views.generic import ListView
from .models import Participante

# Create your views here.

class ParticipanteListView(ListView):
	model = Participante