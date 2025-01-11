from django.shortcuts import render

from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms.models import BaseModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from common.services.get import GetById, GetAll

liste_urls = [
            {"url": "home_common", "label": "Accueil"},
            {"url": "etudiant-infos", "label": "Mes informations"},
            {"url": "etudiant-soutenances", "label": "Mes soutenances"},
            {"url": "logout_common", "label": "Se déconnecter"},
        ]

class HomeView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['menu_items'] = liste_urls
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class InfoEtudiantView(TemplateView):
    template_name = "app_etudiant/etudiant_informations.html"

    def get_context_data(self, **kwargs):
        context = super(InfoEtudiantView, self).get_context_data(**kwargs)
        context['menu_items'] = liste_urls
        id_user = self.request.COOKIES.get("user_data").split(":")[0]
        context['etudiant'] = GetById.get_etudiant_by_id(id_user)
        return context
    
class SoutenancesListView(TemplateView):
    template_name = 'app_etudiant/etudiant_soutenances.html'

    def get_context_data(self, **kwargs):
        id_user = self.request.COOKIES.get("user_data").split(":")[0]
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = get_soutenance_by_etudiant_id(id_user)
        
        context = super(SoutenancesListView, self).get_context_data(**kwargs)
        context["user"] = user
        context["soutenances"] = soutenances
        context["GetById"] = GetById
        context["menu_items"] = liste_urls
        return context
    
@staticmethod
def get_soutenance_by_etudiant_id(id: int) -> list:
    list_soutenance = []
    for soutenance in GetAll.get_all_soutenance():
        if( soutenance.stg_alt.etudiant.id_etu == id):
            list_soutenance.append(soutenance)
    return list_soutenance
    
def get_user(cookie):
        id_user = cookie.split(":")[0]
        type_user = cookie.split(":")[1]
        if type_user == "tuteur_pro":
            return GetById.get_tuteur_pro_by_id(id_user)