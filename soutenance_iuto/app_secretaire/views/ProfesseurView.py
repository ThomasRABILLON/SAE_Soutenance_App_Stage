from django.views.generic import TemplateView

from common.services.get import GetAll, GetById
from common.services.update import Update

from app_secretaire.utils.user_management import get_user, redirect_user
from app_secretaire.constants import URL_LIST

class ProfesseurView(TemplateView):
    template_name = 'app_secretaire/gestion_professeur.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        professeurs = GetAll.get_all_professeur()

        nb_stage_suivi_2 = {}
        nb_stage_suivi_3 = {}
        nb_alternant_suivi_2 = {}
        nb_alternant_suivi_3 = {}

        nb_stg_2_sout_place = {}
        nb_alt_2_sout_place = {}
        nb_stg_3_sout_place = {}
        nb_alt_3_sout_place = {}

        nb_stg_2_sout_candide = {}
        nb_alt_2_sout_candide = {}
        nb_stg_3_sout_candide = {}
        nb_alt_3_sout_candide = {}

        for prof in professeurs:
            nb_stage_suivi_2[prof.id_prof] = GetById.get_nb_stagiaire_suivi_2_annee_professeur(prof.id_prof)
            nb_stage_suivi_3[prof.id_prof] = GetById.get_nb_stagiaire_suivi_3_annee_professeur(prof.id_prof)
            nb_alternant_suivi_2[prof.id_prof] = GetById.get_nb_alternant_suivi_2_annee_professeur(prof.id_prof)
            nb_alternant_suivi_3[prof.id_prof] = GetById.get_nb_alternant_suivi_3_annee_professeur(prof.id_prof)

            nb_stg_2_sout_place[prof.id_prof] = GetById.get_nb_soutenance_stagiaire_2_annee_placer_by_prof_id(prof.id_prof)
            nb_alt_2_sout_place[prof.id_prof] = GetById.get_nb_soutenance_alternant_2_annee_placer_by_prof_id(prof.id_prof)
            nb_stg_3_sout_place[prof.id_prof] = GetById.get_nb_soutenance_stagiaire_3_annee_placer_by_prof_id(prof.id_prof)
            nb_alt_3_sout_place[prof.id_prof] = GetById.get_nb_soutenance_alternant_3_annee_placer_by_prof_id(prof.id_prof)

            nb_stg_2_sout_candide[prof.id_prof] = GetById.get_nb_soutenance_stagiaire_2_annee_candide_by_prof_id(prof.id_prof)
            nb_alt_2_sout_candide[prof.id_prof] = GetById.get_nb_soutenance_alternant_2_annee_candide_by_prof_id(prof.id_prof)
            nb_stg_3_sout_candide[prof.id_prof] = GetById.get_nb_soutenance_stagiaire_3_annee_candide_by_prof_id(prof.id_prof)
            nb_alt_3_sout_candide[prof.id_prof] = GetById.get_nb_soutenance_alternant_3_annee_candide_by_prof_id(prof.id_prof)
        
        context = super(ProfesseurView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["professeurs"] = professeurs
        context["GetById"] = GetById
        context["menu_items"] = URL_LIST
        context["range4"] = range(4)

        context["nb_stage_suivi_2"] = nb_stage_suivi_2
        context["nb_alternant_suivi_2"] = nb_alternant_suivi_2
        context["nb_stage_suivi_3"] = nb_stage_suivi_3
        context["nb_alternant_suivi_3"] = nb_alternant_suivi_3

        context["nb_stg_2_sout_place"] = nb_stg_2_sout_place
        context["nb_alt_2_sout_place"] = nb_alt_2_sout_place
        context["nb_stg_3_sout_place"] = nb_stg_3_sout_place
        context["nb_alt_3_sout_place"] = nb_alt_3_sout_place

        context["nb_stg_2_sout_candide"] = nb_stg_2_sout_candide
        context["nb_alt_2_sout_candide"] = nb_alt_2_sout_candide
        context["nb_stg_3_sout_candide"] = nb_stg_3_sout_candide
        context["nb_alt_3_sout_candide"] = nb_alt_3_sout_candide
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(ProfesseurView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        id_prof = request.POST.get("id_prof")
        nb_stagaire_but2 = request.POST.get("nb_stagaire_but2")
        nb_alternant_but2 = request.POST.get("nb_alternant_but2")
        nb_stagaire_but3 = request.POST.get("nb_stagaire_but3")
        nb_alternant_but3 = request.POST.get("nb_alternant_but3")

        prof = GetById.get_professeur_by_id(id_prof)
        prof.nb_stagaire_but2 = nb_stagaire_but2 if nb_stagaire_but2 else 0
        prof.nb_alternant_but2 = nb_alternant_but2 if nb_alternant_but2 else 0
        prof.nb_stagaire_but3 = nb_stagaire_but3 if nb_stagaire_but3 else 0
        prof.nb_alternant_but3 = nb_alternant_but3 if nb_alternant_but3 else 0

        if Update.update_professeur(prof):
            return self.render_to_response(self.get_context_data())

        print("Erreur lors de la modification")
        return self.render_to_response(self.get_context_data())