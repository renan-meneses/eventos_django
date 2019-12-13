from django.urls import path
from .views import ParticipanteListView
urlpatterns = [
    path('',ParticipanteListView.as_view(), name='participantes'),
    ]