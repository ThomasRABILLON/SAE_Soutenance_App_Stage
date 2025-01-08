from django.db import models

from common.models.Soutenance import Soutenance
from common.models.Professeur import Professeur

class InscriptionSoutenance(models.Model):
    class Meta:
        verbose_name = "InscriptionSoutenance"
    
    soutenance = models.ForeignKey(Soutenance, on_delete=models.CASCADE, null=True)
    prof = models.ForeignKey(Professeur, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'sout={self.soutenance} -> prof={self.prof}'
