from django.db import models

class Entreprise(models.Model):
    class Meta:
        verbose_name = "Entreprise"

    id_etp = models.AutoField(primary_key=True, default=0)
    nom_etp = models.CharField(max_length=255, blank=True, null=True)
    cp_etp = models.CharField(max_length=255, blank=True, null=True)
    ville_etp = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Entreprise(id={self.id_etp}[nom={self.nom_etp},[cp={self.cp_etp},ville={self.ville_etp}]])'
