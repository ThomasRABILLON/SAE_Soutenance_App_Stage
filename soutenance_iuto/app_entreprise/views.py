from django.views.generic import TemplateView
from common.services.get import Get

class InfoEtudiantView(TemplateView):
    template_name = 'app_entreprise/info_etudiant.html'
    
    def get_context_data(self, **kwargs):
        context = super(InfoEtudiantView, self).get_context_data(**kwargs)
        context['etudiant'] = Get.get_etudiant_by_tuteur_pro_id(1)
        return context