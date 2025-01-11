from django.views.generic import TemplateView
from common.services.get import Get, GetById
from django.shortcuts import redirect

def get_user(cookie):
    id_user = cookie.split(":")[0]
    type_user = cookie.split(":")[1]
    if type_user == "tuteur_pro":
        return GetById.get_tuteur_pro_by_id(id_user)
    elif type_user == "etudiant":
        return redirect("etudiant_home")
    elif type_user == "secretaire":
        return redirect("secretaire_home")
    elif type_user == "professeur":
        return redirect("professeur_home")
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
    elif type_user == "professeur":
        return redirect("professeur_home")

class HomeView(TemplateView):
    template_name = 'app_entreprise/home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titre'] = "Accueil"
        user = get_user(self.request.COOKIES['user_data'])
        context['user'] = user
        context["menu_items"] = [
            {"url": "tuteur_pro_home", "label": "Accueil"},
            {"url": "liste_etu_entreprise", "label": "Mes Étudiants"},   
        ]
        return context
    
    def get(self, request, *args, **kwargs):
        if 'user_data' not in request.COOKIES:
            return redirect("login_common")
        return super(HomeView, self).get(request, *args, **kwargs)

class ListeEtudiantView(TemplateView):
    template_name = 'app_entreprise/liste_etudiant.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListeEtudiantView, self).get_context_data(**kwargs)
        context['titre'] = "Mes Étudiants"
        user = get_user(self.request.COOKIES['user_data'])
        context['user'] = user
        context['etudiants'] = Get.get_etudiant_by_tuteur_pro_id(user.id_tut_pro)
        context["menu_items"] = [
            {"url": "tuteur_pro_home", "label": "Accueil"},
            {"url": "liste_etu_entreprise", "label": "Mes Étudiants"},   
        ]
        return context

class InfoEtudiantView(TemplateView):
    template_name = 'app_entreprise/info_etudiant.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupère l'id de l'étudiant depuis l'URL
        etudiant_id = kwargs.get('id_etu')  # Assurez-vous que le paramètre id est passé dans l'URL
        
        if etudiant_id:
            context['etudiant'] = GetById.get_etudiant_by_id(etudiant_id)
        else:
            context['etudiant'] = None  # Si aucun étudiant n'est trouvé, le contexte est vide
            
        context['titre'] = "Informations Étudiant"
        context["menu_items"] = [
            {"url": "tuteur_pro_home", "label": "Accueil"},
            {"url": "liste_etu_entreprise", "label": "Mes Étudiants"},
        ]
        return context

