from django.shortcuts import redirect, render
from common.services.get import GetById
from django.views.generic import TemplateView

from common.views import LoginView

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

class HomeView(TemplateView):
    template_name = "app_professeur/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["menu_items"] = [
            {"url": "professeur_home", "label": "Accueil"},
        ]
        return context
    
    def get(self, request, *args, **kwargs):
        cookie = request.COOKIES.get("user_data")
        if cookie is not None:
            user = get_user(cookie)
            if user is not None:
                return render(request, self.template_name, {"user": user})
        return redirect("login_common")