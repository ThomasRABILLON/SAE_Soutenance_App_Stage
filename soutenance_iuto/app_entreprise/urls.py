from django.urls import path
from . import views


urlpatterns = [
    path('liste_etudiants', views.ListeEtudiantView.as_view(), name='liste_etu_entreprise'),
    path('info_etudiant/<int:id_etu>/', views.InfoEtudiantView.as_view(), name='info_etu_entreprise'),
    path('soutenance/', views.SoutenancesListView.as_view(), name='soutenance_entreprise'),
    path('home/', views.HomeView.as_view(), name='tuteur_pro_home'),
    path('', views.HomeView.as_view(), name='tuteur_pro_home'),
    path('calendrier/', views.CalendarView.as_view(), name='calendrier_entreprise'),
]
