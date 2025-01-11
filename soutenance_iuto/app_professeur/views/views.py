from django.shortcuts import redirect
from django.views.generic import TemplateView

from common.services.get import GetById

def get_user(cookie):
    id_user = cookie.split(":")[0]
    type_user = cookie.split(":")[1]
    if type_user == "professeur":
        return GetById.get_professeur_by_id(id_user)
    elif type_user == "etudiant":
        return redirect("etudiant_home")
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    elif type_user == "secretaire":
        return redirect("secretaire_home")
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
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    
SIDE_BAR_ITEMS = [
    {"url": "professeur_home", "label": "Accueil"},
]

class HomeView(TemplateView):
    template_name = "app_professeur/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["menu_items"] = SIDE_BAR_ITEMS
        context["user"] = get_user(self.request.COOKIES.get("user_data"))
        return context

    def get(self, request, *args, **kwargs):
        response = redirect_user(self.request.COOKIES.get("user_data"))
        if response is not None:
            return response
        return super(HomeView, self).get(request, *args, **kwargs)