from django.urls import path
from . import views


urlpatterns = [
    path('ListeEtudiants', views.ListeEtudiantView.as_view(), name='liste_etu_entreprise'),
    path('InfoEtudiant/<int:id_etu>/', views.InfoEtudiantView.as_view(), name='info_etu_entreprise'),
    path('home/', views.HomeView.as_view(), name='tuteur_pro_home'),
    path('', views.HomeView.as_view(), name='tuteur_pro_home'),
]
