import tempfile

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.files.uploadedfile import InMemoryUploadedFile

from app_secretaire.utils.user_management import get_user, redirect_user
from app_secretaire.constants import URL_LIST

from common.utils.ExternalDataInserter import ExternalDataInserter

class InsertDataView(TemplateView):
    template_name = 'app_secretaire/insert_data.html'

    def get_context_data(self, **kwargs):     
        user = get_user(self.request.COOKIES.get("user_data"))
        
        context = super(InsertDataView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["menu_items"] = URL_LIST
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(InsertDataView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        file = request.POST.get("file")
        if 'file' in request.FILES:
            file: InMemoryUploadedFile = request.FILES['file']
            extension = file.name.split(".")[1].lower()
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=file.name) as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)
                temp_file_path = temp_file.name                
            
            try:
                if extension == 'csv':
                    if 'alternant' in file.name.lower():
                        ExternalDataInserter.alternants_from_csv(temp_file_path)
                    elif 'stage' in file.name.lower():
                        ExternalDataInserter.stagiaires_from_csv(temp_file_path)
                    else:
                        raise Exception("Fichier non reconnu")
                elif extension in ['xls', 'xlsx']:
                    if 'alternant' in file.name.lower():
                        ExternalDataInserter.alternants_from_excel(temp_file_path)
                    elif 'stage' in file.name.lower():
                        ExternalDataInserter.stagiaires_from_excel(temp_file_path)
                    else:
                        raise Exception("Fichier non reconnu")
                else:
                    raise Exception("Fichier non reconnu")
                
                context = self.get_context_data()
                context["success"] = "Données insérées avec succès"
                return self.render_to_response(context)
            except Exception as e:
                context = self.get_context_data()
                context["error"] = "Erreur lors de l'insertion des données : " + str(e)
                return self.render_to_response(context)
            
        context = self.get_context_data()
        context["error"] = "Fichier non trouvé"
        return self.render_to_response(context)

class FileRulesView(TemplateView):
    template_name = 'app_secretaire/file_rules.html'

    def get_context_data(self, **kwargs):     
        user = get_user(self.request.COOKIES.get("user_data"))
        
        context = super(FileRulesView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["menu_items"] = URL_LIST
        return context
    
    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(FileRulesView, self).get(request, *args, **kwargs)