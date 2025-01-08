from django.db import models
from django.utils import timezone

from common.models.Entreprise import Entreprise
from common.models.TuteurPro import TuteurPro
from common.models.Professeur import Professeur
from common.models.Etudiant import Etudiant

class StageAlt(models.Model):
    class Meta:
        verbose_name = "StageAlt"

    id_stg_alt = models.AutoField(primary_key=True, default=0)
    titre_stg_alt = models.CharField(max_length=255, blank=True, null=True)
    theme_stg_alt = models.CharField(max_length=255, blank=True, null=True)
    intitule_env_stg_alt = models.CharField(max_length=255, blank=True, null=True)
    dt_date_debut_stg_alt = models.DateField()
    dt_date_fin_stg_alt = models.DateField()
    duree_stg_alt = models.IntegerField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, null=True)
    tuteur_pro = models.ForeignKey(TuteurPro, on_delete=models.CASCADE, null=True)
    tuteur_univ = models.ForeignKey(Professeur, on_delete=models.CASCADE, null=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'StageAlt(id={self.id_stg_alt}[titre={self.titre_stg_alt},theme={self.theme_stg_alt},intitule_env={self.intitule_env_stg_alt}, [date_debut={self.dt_date_debut_stg_alt},date_fin={self.dt_date_fin_stg_alt},duree={self.duree_stg_alt}], entreprise={self.entreprise},tuteur_pro={self.tuteur_pro},tuteur_univ={self.tuteur_univ},etudiant={self.etudiant}])'
