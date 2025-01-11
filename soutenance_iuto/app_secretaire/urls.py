from django.urls import path

from app_secretaire.views.HomeView import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home_secretaire"),
    path('home/', HomeView.as_view(), name="home_secretaire"),
]
