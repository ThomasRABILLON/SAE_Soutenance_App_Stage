from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

from common.utils.ExternalDataInserter import ExternalDataInserter
from common.services.get import Get

DUREE_COOKIE = 5400

class BaseView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        # ExternalDataInserter.alternants_from_csv('../data_test/alternant/Alternant - BUT3 Sujet.csv')
        # ExternalDataInserter.stagiaires_from_csv('../data_test/stagiaire/tableur stages 2023 2024 extraction AREXIS.xls - Extraction.csv')
        context = super(BaseView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        
        user_data = self.request.COOKIES.get("user_data")
        if user_data is None:
            context["menu_items"] = [
                {"url": "login_common", "label": "Se connecter"},
            ]
            return context
        context["menu_items"] = [
            {"url": "logout_common", "label": "Se déconnecter"},
        ]
        return context


class LoginView(TemplateView):
    template_name = "common/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        id_connection = request.POST.get("username")

        user = Get.get_etudiant_by_id_connection(id_connection)
        print(user)
        if user is not None:
            # response = redirect('etudiant_home')
            response = redirect("home_common")
            response.set_cookie(
                key="user_data",
                value=f"{user.id_etu}:etudiant",
                max_age=DUREE_COOKIE,
                httponly=True,
            )
            return response

        user = Get.get_professeur_by_id_connection(id_connection)
        if user is not None:
            # response = redirect('professeur_home')
            response = redirect("professeur_home")
            response.set_cookie(
                key="user_data",
                value=f"{user.id_prof}:professeur",
                max_age=DUREE_COOKIE,
                httponly=True,
            )
            return response

        user = Get.get_tuteur_pro_by_id_connection(id_connection)
        if user is not None:
            # response = redirect('tuteur_pro_home')
            response = redirect("home_common")
            response.set_cookie(
                key="user_data",
                value=f"{user.id_tut_pro}:tuteur_pro",
                max_age=DUREE_COOKIE,
                httponly=True,
            )
            return response

        user = Get.get_secretaire_by_id_connection(id_connection)
        if user is not None:
            response = redirect('home_secretaire')
            response.set_cookie(
                key="user_data",
                value=f"{user.id_sec}:secretaire",
                max_age=DUREE_COOKIE,
                httponly=True,
            )
            return response
        
        # renvoie sur la page de login si l'utilisateur n'est pas trouvé avec le message d'erreur
        context = self.get_context_data()
        context["error"] = "Identifiant incorrect"
        return self.render_to_response(context)

class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        response = redirect("home_common")
        response.delete_cookie("user_data")
        return response
