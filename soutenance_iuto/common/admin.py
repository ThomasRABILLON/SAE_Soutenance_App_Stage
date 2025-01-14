from django.contrib import admin

from common.models.Secretaire import Secretaire
from common.models.Soutenance import Soutenance
from common.models.Salle import Salle
from common.models.DateHoraire import DateHoraire
from common.models.EstResponsable import EstResponsable
from common.models.Professeur import Professeur
from common.models.StageAlt import StageAlt

# Register your models here.

# class SalleAdmin(admin.ModelAdmin):
#     model = Salle
#     list_display = ['nom_salle', 'id_salle']
#     list_editable = ['id_salle']

class StgAltAdmin(admin.ModelAdmin):
    model = StageAlt
    list_display = ['id_stg_alt', 'tuteur_univ']
    list_editable = ['tuteur_univ']

admin.site.register(Secretaire)
admin.site.register(Soutenance)
admin.site.register(Salle)
admin.site.register(DateHoraire)
admin.site.register(EstResponsable)
admin.site.register(Professeur)
admin.site.register(StageAlt, StgAltAdmin)
