from django.shortcuts import redirect
from common.services.get import GetById

def get_user(cookie):
    id_user = cookie.split(":")[0]
    type_user = cookie.split(":")[1]
    if type_user == "secretaire":
        return GetById.get_secretaire_by_id(id_user)
    elif type_user == "etudiant":
        return redirect("etudiant_home")
    elif type_user == "tuteur_pro":
        return redirect("tuteur_pro_home")
    elif type_user == "professeur":
        return redirect("professeur_home")
    else:
        return redirect("login_common")