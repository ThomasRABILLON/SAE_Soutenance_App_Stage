from django.db import models

from common.models.Professeur import Professeur
from common.models.Promotion import Promotion

class EstResponsable(models.Model):
    class Meta:
        verbose_name = "EstResponsable"

    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, null=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'prof={self.professeur} -> promo={self.promotion}'
