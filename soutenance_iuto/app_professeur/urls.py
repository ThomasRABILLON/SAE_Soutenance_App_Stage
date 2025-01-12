from django.urls import path
from app_professeur.views import views


urlpatterns = [
    path("home/", views.HomeView.as_view(), name="professeur_home"),
    path("profile/", views.ProfileView.as_view(), name="professeur_profile"),
    path("soutenances/", views.SoutenancesByProfView.as_view(), name="professeur_soutenances"),
    path("soutenances_without_candides/", views.SoutenancesWithoutCandidesView.as_view(), name="professeur_soutenances_without_candides"),
    path("studients_by_prof/", views.StudientsByProfView.as_view(), name="students_by_prof"),
]
