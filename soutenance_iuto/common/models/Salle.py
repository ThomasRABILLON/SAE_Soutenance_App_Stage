from django.db import models

class Salle(models.Model):
    class Meta:
        verbose_name = "Salle"

    id_salle = models.AutoField(primary_key=True)
    nom_salle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Salle(id={self.id_salle}[nom={self.nom_salle}])'
