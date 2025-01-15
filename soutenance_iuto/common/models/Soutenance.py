from django.db import models

from common.models.StageAlt import StageAlt
from common.models.DateHoraire import DateHoraire
from common.models.Salle import Salle
from common.models.Professeur import Professeur

class Soutenance(models.Model):
    class Meta:
        verbose_name = "Soutenance"

    id_sout = models.AutoField(primary_key=True, default=0)
    stg_alt = models.ForeignKey(StageAlt, on_delete=models.CASCADE, null=True)
    horaire = models.ForeignKey(DateHoraire, on_delete=models.CASCADE, null=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, null=True)
    prof_candide = models.ForeignKey(Professeur, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Soutenance(id={self.id_sout}[stg={self.stg_alt}, hor={self.horaire}, salle={self.salle}, prof={self.prof_candide}])'
