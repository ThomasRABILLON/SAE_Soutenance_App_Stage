from django.urls import path
from . import views


urlpatterns = [
    path('InfoEtudiant', views.InfoEtudiantView.as_view(), name='info_etu_entreprise'),
    path('home/', views.HomeView.as_view(), name='tuteur_pro_home'),
    path('', views.HomeView.as_view(), name='tuteur_pro_home'),
]
