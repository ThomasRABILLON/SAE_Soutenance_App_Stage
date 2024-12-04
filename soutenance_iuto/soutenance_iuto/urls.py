"""
URL configuration for soutenance_iuto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.EntrepriseViews import EntrepriseViewSet
from api.views.TuteurProViews import TuteurProViewSet
from api.views.EtudiantViews import EtudiantViewSet
from api.views.ProfesseurViews import ProfesseurViewSet
from api.views.EstDansPromotionViews import EstDansPromotionViewSet
from api.views.DateHoraireViews import DateHoraireViewSet
from api.views.EstResponsableViews import EstResponsableViewSet
from api.views.InscriptionSoutenanceViews import InscriptionSoutenanceViewSet
from api.views.InscriptionSuiviViews import InscriptionSuiviViewSet
from api.views.PromotionViews import PromotionViewSet
from api.views.SalleViews import SalleViewSet
from api.views.SecretaireViews import SecretaireViewSet
from api.views.SoutenanceViews import SoutenanceViewSet
from api.views.StageAltViews import StageAltViewSet

router = DefaultRouter()
router.register(r'entreprises',EntrepriseViewSet)
router.register(r'tuteurpros',TuteurProViewSet)
router.register(r'etudiants',EtudiantViewSet)
router.register(r'professeurs',ProfesseurViewSet)
router.register(r'estdanspromotion',EstDansPromotionViewSet)
router.register(r'datehoraire', DateHoraireViewSet)
router.register(r'estresponsable',EstResponsableViewSet)
router.register(r'inscriptionsoutenance', InscriptionSoutenanceViewSet)
router.register(r'inscriptionsuivi', InscriptionSuiviViewSet)
router.register(r'promotion',PromotionViewSet)
router.register(r'salle',SalleViewSet)
router.register(r'secretaires',SecretaireViewSet)
router.register(r'soutenance', SoutenanceViewSet)
router.register(r'stagealt',StageAltViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]
