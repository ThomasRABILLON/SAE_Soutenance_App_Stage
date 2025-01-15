from django.db import models

class Secretaire(models.Model):
    class Meta:
        verbose_name = "Secretaire"
    
    id_sec = models.AutoField(primary_key=True, default=0)
    id_connection = models.CharField(max_length=255, blank=True, null=True)
    nom_sec = models.CharField(max_length=255, blank=True, null=True)
    prenom_sec = models.CharField(max_length=255, blank=True, null=True)
    mail_sec = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'Secretaire(id={self.id_sec}[nom={self.nom_sec},prenom={self.prenom_sec},mail={self.mail_sec}])'
