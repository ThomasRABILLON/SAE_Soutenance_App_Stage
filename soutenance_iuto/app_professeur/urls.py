from django.urls import path
from app_professeur.views import views


urlpatterns = [
    path("home/", views.HomeView.as_view(), name="professeur_home"),
    path("profile/", views.ProfileView.as_view(), name="professeur_profile"),
    path("soutenances/", views.SoutenancesByProfView.as_view(), name="professeur_soutenances"),
    path("soutenance/<int:page>/", views.SoutenancesByProfView.as_view(), name="professeur_soutenance"),
    path("soutenances_without_candides/", views.SoutenancesWithoutCandidesView.as_view(), name="professeur_soutenances_without_candides"),
    path("soutenances_without_candides/<int:page>/", views.SoutenancesWithoutCandidesView.as_view(), name="professeur_soutenances_without_candides"),
    path("etudiants/", views.StudientsByProfView.as_view(), name="prof_etudiants"),
]
