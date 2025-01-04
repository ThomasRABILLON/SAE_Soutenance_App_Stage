from django.db import models
from django.utils import timezone

from common.models.StageAlt import StageAlt
from common.models.Professeur import Professeur

class InscriptionSuivi(models.Model):
    class Meta:
        verbose_name = "InscriptionSuivi"

    stg_alt = models.ForeignKey(StageAlt, on_delete=models.CASCADE, null=True)
    prof = models.ForeignKey(Professeur, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'stage={self.stg_alt} -> prof={self.prof}'
