import tempfile

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.files.uploadedfile import InMemoryUploadedFile

from app_secretaire.constants import URL_LIST

from common.utils.ExternalDataInserter import ExternalDataInserter

from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
import locale

    
class CalendarView(TemplateView):
    template_name = 'app_secretaire/calendar.html'

    def get_context_data(self, **kwargs):
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        context = super().get_context_data(**kwargs)
        context["menu_items"] = URL_LIST

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