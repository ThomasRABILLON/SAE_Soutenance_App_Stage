from django.contrib import admin

from common.models.Secretaire import Secretaire
from common.models.Soutenance import Soutenance
from common.models.Salle import Salle
from common.models.DateHoraire import DateHoraire
from common.models.Promotion import Promotion
from common.models.EstDansPromotion import EstDansPromotion
from common.models.Professeur import Professeur

# Register your models here.

# class SalleAdmin(admin.ModelAdmin):
#     model = Salle
#     list_display = ['nom_salle', 'id_salle']
#     list_editable = ['id_salle']

admin.site.register(Secretaire)
admin.site.register(Soutenance)
admin.site.register(Salle)
admin.site.register(DateHoraire)
admin.site.register(Promotion)
admin.site.register(EstDansPromotion)
admin.site.register(Professeur)