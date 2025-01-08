from django.db import models

from common.models.Entreprise import Entreprise

class TuteurPro(models.Model):
    class Meta:
        verbose_name = "TuteurPro"

    id_tut_pro = models.AutoField(primary_key=True, default=0)
    civilite_tut_pro = models.CharField(max_length=255, blank=True, null=True)
    nom_tut_pro = models.CharField(max_length=255, blank=True, null=True)
    prenom_tut_pro = models.CharField(max_length=255, blank=True, null=True)
    tel_tut_pro = models.CharField(max_length=10, blank=True, null=True)
    gsm_tut_pro = models.CharField(max_length=10, blank=True, null=True)
    mail_tut_pro = models.EmailField(max_length=255, blank=True, null=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'TuteurPro(id={self.id_tut_pro}[civilite={self.civilite_tut_pro},nom={self.nom_tut_pro},prenom={self.prenom_tut_pro},tel={self.tel_tut_pro},gsm={self.gsm_tut_pro},mail={self.mail_tut_pro},entreprise={self.entreprise}])'