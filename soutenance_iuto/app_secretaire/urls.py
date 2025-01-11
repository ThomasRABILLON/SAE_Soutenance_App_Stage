from django.urls import path

from app_secretaire.views.HomeView import HomeView
from app_secretaire.views.SoutenancesViews import SoutenancesListView, SoutenanceCreateView

urlpatterns = [
    path('', HomeView.as_view(), name="home_secretaire"),
    path('home/', HomeView.as_view(), name="home_secretaire"),
    path('soutenances/', SoutenancesListView.as_view(), name="soutenances_secretaire"),
    path('soutenances/create/', SoutenanceCreateView.as_view(), name="soutenance_create_secretaire"),
]
