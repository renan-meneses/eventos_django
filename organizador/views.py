from django.shortcuts import render
from django.views.generic import ListView
from .models import Organizador

# Create your views here.

class OrganizadorListView(ListView):
	model = Organizador
# Create your views here.
