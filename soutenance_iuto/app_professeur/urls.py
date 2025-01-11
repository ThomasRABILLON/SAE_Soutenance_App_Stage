from django.urls import path
from app_professeur.views import views


urlpatterns = [
    path("home/", views.HomeView.as_view(), name="professeur_home"),
]
