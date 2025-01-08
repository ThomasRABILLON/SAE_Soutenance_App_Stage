from django.urls import path
from django.contrib import admin
from app_etudiant.views import views
from django.views.generic import *


urlpatterns = [
    #path('etudiant-home', views.HomeView.as_view(), name='etudiant-home'),
    path("etudiant-home/", views.HomeView.as_view(), name="etudiant-home"),
    # path('etudiant-login', views.etudiant_login, name='etudiant-login'),
    # path('etudiant-register', views.etudiant_register, name='etudiant-register'),
]