from django.urls import path
from app_professeur.views import views


urlpatterns = [
    path("home/", views.HomeView.as_view(), name="professeur_home"),
    path("profile/", views.ProfileView.as_view(), name="professeur_profile"),
    path("soutenances/", views.SoutenancesByProfView.as_view(), name="professeur_soutenances"),
    path("soutenance/<int:page>/", views.SoutenancesByProfView.as_view(), name="professeur_soutenance"),
    path("soutenances_sans_candides/", views.SoutenancesWithoutCandidesView.as_view(), name="professeur_soutenances_without_candides"),
    path("soutenances_sans_candides/<int:page>/", views.SoutenancesWithoutCandidesView.as_view(), name="professeur_soutenances_without_candides"),
    path("inscription_soutenance/<int:id_sout>", views.InscriptionSoutenanceView.as_view(), name="professeur_inscription_soutenance"),
    path("desinscription_soutenance/<int:id_sout>", views.DesinscriptionSoutenanceView.as_view(), name="professeur_desinscription_soutenance"),
    path("etudiants/", views.StudientsByProfView.as_view(), name="prof_etudiants"),
    path("stages/", views.StageListView.as_view(), name="stages"),
    path("stages/<int:page>", views.StageListView.as_view(), name="stage"),
    path("stage_inscritption/<int:id_stage>", views.InscriptionStageView.as_view(), name="stage_inscription"),
    path("stage_desinscription/<int:id_stage>", views.DesinscriptionStageView.as_view(), name="stage_desinscription"),
    path("detail_stagiaire/<int:id_etu>", views.StageDetailsView.as_view(), name="detail_stage"),
    path("calendrier/", views.CalendarView.as_view(), name="calendrier_professeur"),
]
