from django.urls import path
from .views import OrganizadorListView

urlpatterns = [
    path('', OrganizadorListView.as_view(), name='organizador'),
    ]