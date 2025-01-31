from django.urls import path
from django.contrib import admin
from app_etudiant.views import views
from django.views.generic import *


urlpatterns = [
    path("", views.HomeView.as_view(), name="etudiant-home"),
    path("home/", views.HomeView.as_view(), name="etudiant-home"),
    path("informations/", views.InfoEtudiantView.as_view(), name="etudiant-infos"),
    path("soutenances/", views.SoutenancesListView.as_view(), name="etudiant-soutenances"),
    path("calendrier/", views.CalendarView.as_view(), name="calendrier_etudiant"),
]