from django.views.generic import TemplateView

from app_secretaire.utils.get_user import get_user

class HomeView(TemplateView):
    template_name = 'app_secretaire/home.html'

    def get_context_data(self, **kwargs):     
        user = get_user(self.request.COOKIES.get("user_data"))
        
        context = super(HomeView, self).get_context_data(**kwargs)
        context["title"] = "IUT Orleans"
        context["user"] = user
        context["menu_items"] = [
            # {"url": "login_common", "label": "Se connecter"},
        ]
        return context