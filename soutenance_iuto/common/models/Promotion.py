from django.db import models
from django.utils import timezone

class Promotion(models.Model):
    class Meta:
        verbose_name = "Promotion"

    id_promo = models.AutoField(primary_key=True, default=0)
    annee_promo = models.IntegerField(default=timezone.now().year)
    filiere_promo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Promotion(id={self.id_promo}[annee={self.annee_promo},filiere={self.filiere_promo}])'
