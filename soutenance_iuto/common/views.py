from django.views.generic import TemplateView

from common.utils.ExternalDataInserter import ExternalDataInserter

class BaseView(TemplateView):
    template_name = 'common/base.html'

    def get_context_data(self, **kwargs):
        # ExternalDataInserter.alternants_from_csv('../data_test/alternant/Alternant - BUT3 Sujet.csv')
        # ExternalDataInserter.stagiaires_from_csv('../data_test/stagiaire/tableur stages 2023 2024 extraction AREXIS.xls - Extraction.csv')
        context = super(BaseView, self).get_context_data(**kwargs)
        context['title'] = 'IUT Orleans'
        context['menu_items'] = [
        {"url": "/etudiants/", "label": "Liste des étudiants"},
        {"url": "/soutenances/", "label": "Tableau des soutenances"},
        {"url": "/planning/", "label": "Planning"}
    ]
        return context