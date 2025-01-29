from django.shortcuts import redirect
from django.views.generic import TemplateView

from common.services.get import GetById, Get, GetAll
from common.services.update import Update
from common.services.insert import Insert
from common.services.delete import Delete

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
    {"url": "professeur_home", "label": "Mon espace"},
    {"url": "prof_etudiants", "label": "Mes étudiants"},
    {"url": "professeur_soutenances", "label": "Mes soutenances"},
    {"url": "stages", "label": "Les stages sans tuteur"},
    {"url": "professeur_soutenances_without_candides", "label": "Les soutenances sans candides"},
    {"url": "logout_common", "label": "Se déconnecter"},
]

class HomeView(TemplateView):
    template_name = "app_professeur/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["nb_soutenance_candide"] = GetById.get_nb_soutenance_candide_by_prof_id(context["user"].id_prof)
        context["nb_soutenance_tutore"] = GetById.get_nb_soutenance_tutored_by_prof_id(context["user"].id_prof)
        context["nb_soutenance_candide_total"] = GetAll.get_all_soutenance_candide()
        # Information du dashboard
        context["nb_statgiaire_suivre"] = Get.get_nombre_stagiaire_a_suivre()
        context["nb_stagiaire_suivie"] = GetById.get_nb_stagiaire_suivi_professeur(context["user"].id_prof)
        context["nb_stagiare_3_annee_suivre"] = Get.get_nombre_stagiaire_3_annee_a_suivre()
        context["nb_statgiaire_3_annee_suivie"] = GetById.get_nb_stagiaire_suivi_3_annee_professeur(context["user"].id_prof)
        context["nb_soutenance_3_annee_suivie"] = GetById.get_nb_soutenance_stagiaire_3_annee_candide_by_prof_id(context["user"].id_prof)
        context["nb_stagiare_2_annee_suivre"] = Get.get_nombre_stagiaire_2_annee_a_suivre()
        context["nb_statgiaire_2_annee_suivie"] = GetById.get_nb_stagiaire_suivi_2_annee_professeur(context["user"].id_prof)
        context["nb_soutenance_2_annee_suivie"] = GetById.get_nb_soutenance_stagiaire_2_annee_candide_by_prof_id(context["user"].id_prof)
        #Alternant
        context["nb_alternant_suivre"] = Get.get_nombre_alternant_a_suivre()
        context["nb_alternant_suivie"] = GetById.get_nb_alternant_suivi_professeur(context["user"].id_prof)
        context["nb_alternant_3_annee_suivre"] = Get.get_nombre_alternant_3_annee_a_suivre()
        context["nb_alternant_3_annee_suivie"] = GetById.get_nb_alternant_suivi_3_annee_professeur(context["user"].id_prof)
        context["nb_soutenance_3_annee_suivie"] = GetById.get_nb_soutenance_alternant_3_annee_candide_by_prof_id(context["user"].id_prof)
        context["nb_alternant_2_annee_suivre"] = Get.get_nombre_alternant_2_annee_a_suivre()
        context["nb_alternant_2_annee_suivie"] = GetById.get_nb_alternant_suivi_2_annee_professeur(context["user"].id_prof)
        context["nb_soutenance_2_annee_suivie"] = GetById.get_nb_soutenance_alternant_2_annee_candide_by_prof_id(context["user"].id_prof)
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
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = Get.get_all_soutenance_prof(user.id_prof)
        est_dans_promotion = GetAll.get_all_est_dans_promotion()
        
        page = 1
        nb_pages = len(soutenances) // 7 + 1
        if kwargs.get("page") is not None:
            page = kwargs.get("page")
        soutenances = soutenances[(page - 1) * 7:page * 7]
        
        context = super(SoutenancesByProfView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["soutenances"] = soutenances
        context["est_dans_promotion"] = est_dans_promotion
        context["GetById"] = GetById
        context["page"] = page
        context["nb_pages"] = nb_pages
        context["range"] = range(1, nb_pages + 1)
        context["previous_page"] = page - 1
        context["next_page"] = page + 1
        context["url"] = "professeur_soutenances"
        context["menu_items"] = SIDE_BAR_ITEMS
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenancesByProfView, self).get(request, *args, **kwargs)

class InscriptionSoutenanceView(TemplateView):
    template_name = "app_professeur/inscription_desinscription_soutenance.html"
    
    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_sout = kwargs.get("id_sout")
        
        context = super(InscriptionSoutenanceView, self).get_context_data(**kwargs)
        context["user"] = user
        context["question"] = "Êtes-vous sûr de vouloir vous inscrire à cette soutenance ?"
        context["url_form"] = "professeur_inscription_soutenance"
        context["soutenance"] = GetById.get_soutenance_by_id(id_sout)
        context["menu_items"] = SIDE_BAR_ITEMS
        return context
    
    def post(self, request, *args, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_sout = kwargs.get("id_sout")
        
        if id_sout is not None:
            sout = GetById.get_soutenance_by_id(id_sout)
            if sout is not None:
                sout.prof_candide = user
                Update.update_soutenance(sout)
        return redirect("professeur_soutenances")
    
class DesinscriptionSoutenanceView(TemplateView):
    template_name = "app_professeur/inscription_desinscription_soutenance.html"
    
    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_sout = kwargs.get("id_sout")
        
        context = super(DesinscriptionSoutenanceView, self).get_context_data(**kwargs)
        context["user"] = user
        context["question"] = "Êtes-vous sûr de vouloir vous désinscrire de cette soutenance ?"
        context["url_form"] = "professeur_desinscription_soutenance"
        context["soutenance"] = GetById.get_soutenance_by_id(id_sout)
        context["menu_items"] = SIDE_BAR_ITEMS
        return context
    
    def post(self, request, *args, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_sout = kwargs.get("id_sout")
        
        if id_sout is not None:
            sout = GetById.get_soutenance_by_id(id_sout)
            if sout is not None:
                sout.prof_candide = None
                Update.update_soutenance(sout)
        return redirect("professeur_soutenances")

class SoutenancesWithoutCandidesView(TemplateView):
    template_name = "app_professeur/soutenances.html"

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = Get.get_all_soutenance_without_candide(user.id_prof)
        est_dans_promotion = GetAll.get_all_est_dans_promotion()
        
        page = 1
        nb_pages = len(soutenances) // 10 + 1
        if kwargs.get("page") is not None:
            page = kwargs.get("page")
        soutenances = soutenances[(page - 1) * 10:page * 10]
        
        context = super(SoutenancesWithoutCandidesView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["soutenances"] = soutenances
        context["est_dans_promotion"] = est_dans_promotion
        context["GetById"] = GetById
        context["page"] = page
        context["nb_pages"] = nb_pages
        context["range"] = range(1, nb_pages + 1)
        context["previous_page"] = page - 1
        context["next_page"] = page + 1
        context["url"] = "professeur_soutenances_without_candides"
        context["menu_items"] = SIDE_BAR_ITEMS
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
        context["etudiants"] = Get.get_all_studients_by_tuteur_univ(context["user"].id_prof)
        context["est_dans_promotion"] = GetAll.get_all_est_dans_promotion()
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(StudientsByProfView, self).get(request, *args, **kwargs)

class StageListView(TemplateView):
    template_name = "app_professeur/list_stage.html"

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        stages = Get.get_stage_wout_tuteur_pro()
        
        context = super(StageListView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["est_dans_promotion"] = GetAll.get_all_est_dans_promotion()
        
        page = 1
        nb_pages = len(stages) // 5 + 1
        if kwargs.get("page") is not None:
            page = kwargs.get("page")
        stages = stages[(page - 1) * 5:page * 5]
        
        context["inscriptions"] = GetById.get_inscription_suivi_by_prof_id(user.id_prof)
        
        context["stages"] = stages
        context["page"] = page
        context["nb_pages"] = nb_pages
        context["range"] = range(1, nb_pages + 1)
        context["previous_page"] = page - 1
        context["next_page"] = page + 1
        context["url"] = "stage"
        
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(StageListView, self).get(request, *args, **kwargs)

class InscriptionStageView(TemplateView):
    template_name = "app_professeur/inscription_desinscription_suivi_stage.html"
    
    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_stage = kwargs.get("id_stage")
        
        context = super(InscriptionStageView, self).get_context_data(**kwargs)
        context["user"] = user
        context["stage"] = GetById.get_stage_alt_by_id(id_stage)
        context["question"] = "Êtes-vous sûr de vouloir vous désinscrire de ce stage ?"
        context["is_inscription"] = True
        context["menu_items"] = SIDE_BAR_ITEMS
        return context
    
    def post(self, request, *args, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_stage = kwargs.get("id_stage")
        
        if id_stage is not None:
            stage = GetById.get_stage_alt_by_id(id_stage)
            if stage is not None:
                stage.tuteur_univ = user
                Update.update_stage_alt(stage)
        return redirect("stages")
    
class DesinscriptionStageView(TemplateView):
    template_name = "app_professeur/inscription_desinscription_suivi_stage.html"
    
    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_stage = kwargs.get("id_stage")
        
        context = super(DesinscriptionStageView, self).get_context_data(**kwargs)
        context["user"] = user
        context["stage"] = GetById.get_stage_alt_by_id(id_stage)
        context["question"] = "Êtes-vous sûr de vouloir vous désinscrire de ce stage ?"
        context["is_inscription"] = False
        context["menu_items"] = SIDE_BAR_ITEMS
        return context
    
    def post(self, request, *args, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_stage = kwargs.get("id_stage")
        
        if id_stage is not None:
            stage = GetById.get_stage_alt_by_id(id_stage)
            if stage is not None:
                stage.tuteur_univ = None
                Update.update_stage_alt(stage)
        return redirect("stages")
    
class StageDetailsView(TemplateView):
    template_name = "app_professeur/detail_stage.html"

    def get_context_data(self, **kwargs):
        context = super(StageDetailsView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        context["stage"] = Get.get_stage_alt_by_etu_id(kwargs.get("id_etu")).first()
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(StageDetailsView, self).get(request, *args, **kwargs)