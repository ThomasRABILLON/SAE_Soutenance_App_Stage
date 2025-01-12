from django.shortcuts import redirect
from django.views.generic import TemplateView

from common.services.get import GetById, Get

def get_user(cookie):
    id_user = cookie.split(":")[0]
    type_user = cookie.split(":")[1]
    if type_user == "professeur":
        return GetById.get_professeur_by_id(id_user)
    elif type_user == "etudiant":
        return redirect("etudiant_home")
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    elif type_user == "secretaire":
        return redirect("secretaire_home")
    else:
        return redirect("login_common")

def redirect_user(cookie):
    if cookie is None:
        return redirect("login_common")
    type_user = cookie.split(":")[1]
    if type_user == "etudiant":
        return redirect("etudiant_home")
    elif type_user == "secretaire":
        return redirect("secretaire_home")
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    
SIDE_BAR_ITEMS = [
    {"url": "professeur_home", "label": "Accueil"},
    {"url": "professeur_profile", "label": "Profil"},
    {"url": "professeur_soutenances", "label": "Mes soutenances"},
    {"url": "professeur_soutenances_without_candides", "label": "Soutenances sans candides"},
    {"url": "students_by_prof", "label": "Etudiants"},
]

class HomeView(TemplateView):
    template_name = "app_professeur/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(HomeView, self).get(request, *args, **kwargs)

class ProfileView(TemplateView):
    template_name = "app_professeur/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(ProfileView, self).get(request, *args, **kwargs)
    
class SoutenancesByProfView(TemplateView):
    template_name = "app_professeur/soutenances.html"

    def get_context_data(self, **kwargs):
        context = super(SoutenancesByProfView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["soutenances"] = Get.get_all_soutenance_prof(context["user"].id_prof)
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenancesByProfView, self).get(request, *args, **kwargs)

class SoutenancesWithoutCandidesView(TemplateView):
    template_name = "app_professeur/soutenances.html"

    def get_context_data(self, **kwargs):
        context = super(SoutenancesWithoutCandidesView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["soutenances"] = Get.get_all_soutenance_without_candide()
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenancesWithoutCandidesView, self).get(request, *args, **kwargs)

class SoutenanceDetailsView(TemplateView):
    template_name = "app_professeur/soutenance_details.html"

    def get_context_data(self, **kwargs):
        context = super(SoutenanceDetailsView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["soutenance"] = GetById.get_soutenance_by_id(context["user"].id_prof)
        context["candides"] = Get.get_all_candide_by_soutenance(context["soutenance"].id_sout)
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenanceDetailsView, self).get(request, *args, **kwargs)

class StudientsByProfView(TemplateView):
    template_name = "app_professeur/studients_by_prof.html"

    def get_context_data(self, **kwargs):
        context = super(StudientsByProfView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["students"] = Get.get_all_studients_by_tuteur_univ(context["user"].id_prof)
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(StudientsByProfView, self).get(request, *args, **kwargs)