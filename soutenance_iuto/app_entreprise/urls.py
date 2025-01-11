from django.urls import path
from . import views

urlpatterns = [
    path('InfoEtudiant', views.InfoEtudiantView.as_view(), name='info_etu_entreprise'),
]
