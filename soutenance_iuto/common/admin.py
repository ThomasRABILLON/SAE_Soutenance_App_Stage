from django.contrib import admin

from common.models.Secretaire import Secretaire
from common.models.Soutenance import Soutenance
from common.models.Salle import Salle
from common.models.DateHoraire import DateHoraire

# Register your models here.

admin.site.register(Secretaire)
admin.site.register(Soutenance)
admin.site.register(Salle)
admin.site.register(DateHoraire)