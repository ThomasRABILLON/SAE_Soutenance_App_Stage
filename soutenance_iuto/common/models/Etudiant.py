from django.db import models

class Etudiant(models.Model):
    class Meta:
        verbose_name = "Etudiant"
    
    id_etu = models.AutoField(primary_key=True, default=0)
    num_etu = models.CharField(max_length=255, blank=True, null=True)
    ine_etu = models.CharField(max_length=255, blank=True, null=True)
    civilite_etu = models.CharField(max_length=255, blank=True, null=True)
    nom_etu = models.CharField(max_length=255, blank=True, null=True)
    prenom_etu = models.CharField(max_length=255, blank=True, null=True)
    mail_etu = models.EmailField(max_length=255, blank=True, null=True)
    alternant = models.BooleanField(default=False)

    def __str__(self):
        return f'Etudiant(id={self.id_etu}[ine={self.ine_etu},[civilite={self.civilite_etu},nom={self.nom_etu},prenom={self.prenom_etu},mail={self.mail_etu},alternant={self.alternant}]])'
