from django.urls import path

from app_secretaire.views.HomeView import HomeView
from app_secretaire.views.SoutenancesViews import SoutenancesListView, SoutenanceCreateView, SoutenanceDeleteView, SoutenanceUpdateView
from app_secretaire.views.InsertDataView import InsertDataView, FileRulesView
from app_secretaire.views.CalendarView import CalendarView

urlpatterns = [
    path('', HomeView.as_view(), name="home_secretaire"),
    path('home/', HomeView.as_view(), name="home_secretaire"),
    path('soutenances/', SoutenancesListView.as_view(), name="soutenances_secretaire"),
    path('soutenances/<int:page>/', SoutenancesListView.as_view(), name="soutenances_secretaire"),
    path('soutenances/create/', SoutenanceCreateView.as_view(), name="soutenance_create_secretaire"),
    path('soutenances/<int:id_sout>/delete/', SoutenanceDeleteView.as_view(), name="soutenance_delete_secretaire"),
    path('soutenances/<int:id_sout>/update/', SoutenanceUpdateView.as_view(), name="soutenance_update_secretaire"),
    path('insertion_fichier_externe/', InsertDataView.as_view(), name="insert_data_secretaire"),
    path('insertion_fichier_externe/regles/', FileRulesView.as_view(), name="file_rules_secretaire"),
    path('calendrier/', CalendarView.as_view(), name="calendrier_secretaire"),
]
