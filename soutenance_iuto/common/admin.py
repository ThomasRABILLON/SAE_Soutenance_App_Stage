from django.contrib import admin

from common.models.Secretaire import Secretaire
from common.models.Soutenance import Soutenance
from common.models.Salle import Salle
from common.models.DateHoraire import DateHoraire

# Register your models here.

# class SalleAdmin(admin.ModelAdmin):
#     model = Salle
#     list_display = ['nom_salle', 'id_salle']
#     list_editable = ['id_salle']

admin.site.register(Secretaire)
admin.site.register(Soutenance)
admin.site.register(Salle)
admin.site.register(DateHoraire)