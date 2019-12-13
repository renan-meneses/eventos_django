from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento

# Create your views here.

class EventoListView(ListView):
	model = Evento