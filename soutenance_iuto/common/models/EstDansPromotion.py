from django.db import models

from common.models.Etudiant import Etudiant
from common.models.Promotion import Promotion

class EstDansPromotion(models.Model):
    class Meta:
        verbose_name = "EstDansPromotion"

    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'etu={self.etudiant} -> promo={self.promotion}'
