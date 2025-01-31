from django.views.generic import TemplateView
from common.services.get import Get, GetById, GetAll
from django.shortcuts import redirect

from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
import locale

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
    
urls_sidebar= [
            {"url": "tuteur_pro_home", "label": "Mon espace"},
            {"url": "liste_etu_entreprise", "label": "Mes étudiants"},
            {"url": "soutenance_entreprise", "label": "Mes soutenances"},
            {"url": "calendrier_etudiant", "label": "Planning de mes soutenances"},
            {"url": "logout_common", "label": "Se déconnecter"}
        ]

class HomeView(TemplateView):
    template_name = 'app_entreprise/home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titre'] = "Accueil"
        user = get_user(self.request.COOKIES['user_data'])
        context['user'] = user
        context["menu_items"] = urls_sidebar
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
        context["menu_items"] = urls_sidebar
        return context

class InfoEtudiantView(TemplateView):
    template_name = 'app_entreprise/info_etudiant.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupère l'id de l'étudiant depuis l'URL
        etudiant_id = kwargs.get('id_etu')  # Assurez-vous que le paramètre id est passé dans l'URL
        
        if etudiant_id:
            context['etudiant'] = GetById.get_etudiant_by_id(etudiant_id)
            context['stage'] = Get.get_stage_alt_by_etu_id(etudiant_id).first()
        else:
            context['etudiant'] = None  # Si aucun étudiant n'est trouvé, le contexte est vide
            
        context['titre'] = "Informations étudiant"
        context["menu_items"] = urls_sidebar
        return context

class SoutenancesListView(TemplateView):
    template_name = 'app_entreprise/liste_soutenance.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request.COOKIES.get("user_data"))
        soutenances = Get.get_soutenance_by_tuteur_pro_id(user.id_tut_pro)
        est_dans_promotion = GetAll.get_all_est_dans_promotion()
        
        context = super(SoutenancesListView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["soutenances"] = soutenances
        context["est_dans_promotion"] = est_dans_promotion
        context["GetById"] = GetById
        context["menu_items"] = urls_sidebar
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(SoutenancesListView, self).get(request, *args, **kwargs)
    
class CalendarView(TemplateView):
    template_name = 'app_etudiant/calendar.html'

    def get_context_data(self, **kwargs):
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        context = super().get_context_data(**kwargs)
        context["menu_items"] = urls_sidebar

        d = get_date(self.request.GET.get('day', None))
        year = d.year

        # Handle week navigation
        prev_week = d - timedelta(days=7)
        current_week = d
        next_week = d + timedelta(days=7)
        
        context['current_year'] = year

        context['prev_week'] = prev_week.strftime('%Y-%m-%d')
        context['current_week'] = current_week.strftime('%Y-%m-%d')
        context['next_week'] = next_week.strftime('%Y-%m-%d')

        first_day_of_week = d - timedelta(days=d.weekday())

        html_week = '<table class="week-calendar">'
        html_week += f'<thead><tr><th>{d.strftime("%B").capitalize()}</th>'
        for i in range(7):
            day = first_day_of_week + timedelta(days=i)
            html_week += f'<th>{day.strftime("%A %d").capitalize()}</th>'
        html_week += '</tr></thead><tbody>'
        
        for hour in range(8,20):
            html_week += f'<tr><td>{hour}:00</td>'
            for i in range(7):
                html_week += '<td></td>'
            html_week += '</tr>'
        
        html_week += '</tbody></table>'

        context['calendar'] = mark_safe(html_week)
        return context

def get_date(req_day):
    if req_day:
        year, month, day = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day)
    return datetime.today()
