from django.views.generic import TemplateView

class BaseView(TemplateView):
    template_name = 'common/base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['title'] = 'IUT Orleans'
        context['menu_items'] = [
        {"url": "/etudiants/", "label": "Liste des étudiants"},
        {"url": "/soutenances/", "label": "Tableau des soutenances"},
        {"url": "/planning/", "label": "Planning"}
    ]
        return context