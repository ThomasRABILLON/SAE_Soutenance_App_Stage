from django.views.generic import TemplateView
from django.shortcuts import redirect

from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
import locale

from common.services.get import GetById, Get

liste_urls = [
            {"url": "etudiant-home", "label": "Mon espace"},
            {"url": "etudiant-infos", "label": "Mes informations"},
            {"url": "etudiant-soutenances", "label": "Mes soutenances"},
            {"url": "calendrier_etudiant", "label": "Planning de mes soutenances"},
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
        context["stage"] = Get.get_stage_alt_by_etu_id(user.id_etu).first()
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
    
class CalendarView(TemplateView):
    template_name = 'app_etudiant/calendar.html'

    def get_context_data(self, **kwargs):
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        context = super().get_context_data(**kwargs)
        context["menu_items"] = liste_urls

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