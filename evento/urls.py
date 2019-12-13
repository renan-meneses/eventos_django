from django.urls import path
from .views import EventoListView

urlpatterns = [
    path('', EventoListView.as_view(), name='evento'),
    ]