from django.views.generic import TemplateView
from common.services.get import Get, GetById
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = 'app_entreprise/home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titre'] = "Accueil"
        user = get_user(self.request.COOKIES['user_data'])
        context['user'] = user
        return context

class InfoEtudiantView(TemplateView):
    template_name = 'app_entreprise/info_etudiant.html'
    
    def get_context_data(self, **kwargs):
        context = super(InfoEtudiantView, self).get_context_data(**kwargs)
        context['titre'] = "Informations sur l'étudiant"
        context['etudiant'] = Get.get_etudiant_by_tuteur_pro_id(1)
        return context
    
def get_user(cookie):
    id_user = cookie.split(":")[0]
    type_user = cookie.split(":")[1]
    if type_user == "secretaire":
        return GetById.get_secretaire_by_id(id_user)
    elif type_user == "etudiant":
        return redirect("etudiant_home")
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    elif type_user == "professeur":
        return redirect("professeur_home")
    else:
        return redirect("login_common")