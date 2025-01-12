from django.views.generic import TemplateView
from django.shortcuts import redirect

from common.services.get import GetById, Get

liste_urls = [
            {"url": "etudiant-home", "label": "Accueil"},
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

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(HomeView, self).get(request, *args, **kwargs)
    
class InfoEtudiantView(TemplateView):
    template_name = "app_etudiant/etudiant_informations.html"

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        
        context = super(InfoEtudiantView, self).get_context_data(**kwargs)
        context['menu_items'] = liste_urls
        context['etudiant'] = user
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(InfoEtudiantView, self).get(request, *args, **kwargs)
    
class SoutenancesListView(TemplateView):
    template_name = 'app_etudiant/etudiant_soutenances.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = Get.get_soutenance_by_etudiant_id(user.id_etu)
        
        context = super(SoutenancesListView, self).get_context_data(**kwargs)
        context["user"] = user
        context["soutenances"] = soutenances
        context["GetById"] = GetById
        context["menu_items"] = liste_urls
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenancesListView, self).get(request, *args, **kwargs)
    
def get_user(cookie):
    if cookie is not None:
        id_user = cookie.split(":")[0]
        type_user = cookie.split(":")[1]
        if type_user == "etudiant":
            return GetById.get_etudiant_by_id(id_user)
    return None

def redirect_user(cookie):
    if cookie is None:
        return redirect("login_common")
    type_user = cookie.split(":")[1]
    if type_user == "secretaire":
        return redirect("secretaire_home")
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    elif type_user == "professeur":
        return redirect("professeur_home")