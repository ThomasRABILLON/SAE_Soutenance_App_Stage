from django.views.generic import TemplateView, CreateView

from app_secretaire.utils.user_management import get_user, redirect_user
from common.services.get import GetAll, GetById

from app_secretaire.forms import SoutenanceForm
from common.models.Soutenance import Soutenance
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect

class SoutenancesListView(TemplateView):
    template_name = 'app_secretaire/soutenances.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = GetAll.get_all_soutenance()
        est_dans_promotion = GetAll.get_all_est_dans_promotion()
        
        context = super(SoutenancesListView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["soutenances"] = soutenances
        context["est_dans_promotion"] = est_dans_promotion
        context["GetById"] = GetById
        context["menu_items"] = [
            # {"url": "login_common", "label": "Se connecter"},
        ]
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenancesListView, self).get(request, *args, **kwargs)
    
class SoutenanceCreateView(TemplateView):
    template_name = 'app_secretaire/soutenance_create.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        
        context = super(SoutenanceCreateView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["form"] = SoutenanceForm()
        context["menu_items"] = [
            # {"url": "login_common", "label": "Se connecter"},
        ]
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenanceCreateView, self).get(request, *args, **kwargs)