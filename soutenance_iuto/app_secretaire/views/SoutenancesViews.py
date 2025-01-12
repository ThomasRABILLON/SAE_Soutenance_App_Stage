from django.views.generic import TemplateView
from django.shortcuts import redirect

from app_secretaire.utils.user_management import get_user, redirect_user
from common.services.get import GetAll, GetById, Get
from common.services.insert import Insert
from common.services.update import Update
from app_secretaire.constants import URL_LIST

class SoutenancesListView(TemplateView):
    template_name = 'app_secretaire/soutenances.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = GetAll.get_all_soutenance()
        est_dans_promotion = GetAll.get_all_est_dans_promotion()
        
        page = 1
        nb_pages = len(soutenances) // 7 + 1
        if kwargs.get("page") is not None:
            page = kwargs.get("page")
        soutenances = soutenances[(page - 1) * 7:page * 7]
        
        context = super(SoutenancesListView, self).get_context_data(**kwargs)
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
        context["menu_items"] = URL_LIST
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
        context["etudiants"] = GetAll.get_all_etudiant()
        context["salles"] = GetAll.get_all_salle()
        context["menu_items"] = URL_LIST
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenanceCreateView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        id_etu = request.POST.get("etudiant")
        dt_date = request.POST.get("date")
        heure = request.POST.get("heure")
        salle = request.POST.get("salle")
        
        stg_alt = Get.get_stage_alt_by_etu_id(id_etu)[0]
        horaire = Get.get_horaire_by_date_heure(dt_date, heure)
        if horaire is None:
            new_id = Get.get_last_id_date_horaire() + 1
            Insert.insert_date_horaire(dt_date, heure, 1, new_id)
            horaire = GetById.get_date_horaire_by_id(new_id)
        salle = GetById.get_salle_by_id(int(salle))
        
        if Get.get_salle_est_libre(salle.id_salle, horaire.id_date_horaire):
            if Insert.insert_soutenance(stg_alt.id_stg_alt, horaire.id_date_horaire, salle.id_salle, None, Get.get_last_id_soutenance() + 1):
                return redirect("soutenances_secretaire")
            else:
                context = self.get_context_data()
                context["error"] = "Erreur lors de la création de la soutenance"
                return self.render_to_response(context)
        context = self.get_context_data()
        context["error"] = "La salle n'est pas libre à cette date et heure"
        return self.render_to_response(context)

class SoutenanceDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        id_sout = kwargs.get("id_sout")
        soutenance = GetById.get_soutenance_by_id(id_sout)
        
        if soutenance is not None:
            soutenance.delete()
        
        return redirect("soutenances_secretaire")
    
class SoutenanceUpdateView(TemplateView):
    template_name = 'app_secretaire/soutenance_update.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        id_sout = kwargs.get("id_sout")
        soutenance = GetById.get_soutenance_by_id(id_sout)
        
        context = super(SoutenanceUpdateView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["soutenance"] = soutenance
        context["salles"] = GetAll.get_all_salle()
        context["menu_items"] = URL_LIST
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenanceUpdateView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        id_sout = kwargs.get("id_sout")
        dt_date = request.POST.get("date")
        heure = request.POST.get("heure")
        salle = request.POST.get("salle")
        
        soutenance = GetById.get_soutenance_by_id(id_sout)
        horaire = Get.get_horaire_by_date_heure(dt_date, heure)
        if horaire is None:
            new_id = Get.get_last_id_date_horaire() + 1
            Insert.insert_date_horaire(dt_date, heure, 1, new_id)
            horaire = GetById.get_date_horaire_by_id(new_id)
        salle = GetById.get_salle_by_id(int(salle))
        
        
        if Get.get_salle_est_libre(salle.id_salle, horaire.id_date_horaire):
            soutenance.horaire = horaire
            soutenance.salle = salle
            
            if Update.update_soutenance(soutenance):
                return redirect("soutenances_secretaire")
            else:
                context = self.get_context_data(**kwargs)
                context["error"] = "Erreur lors de la modification de la soutenance"
                return self.render_to_response(context)
        
        context = self.get_context_data(**kwargs)
        context["error"] = "La salle n'est pas libre à cette date et heure"
        return self.render_to_response(context)