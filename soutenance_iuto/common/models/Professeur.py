from django.db import models

class Professeur(models.Model):
    class Meta:
        verbose_name = "Professeur"

    id_prof = models.AutoField(primary_key=True, default=0)
    id_connection = models.CharField(max_length=255, blank=True, null=True)
    num_prof = models.CharField(max_length=255, blank=True, null=True)
    civilite_prof = models.CharField(max_length=255, blank=True, null=True)
    nom_prof = models.CharField(max_length=255, blank=True, null=True)
    prenom_prof = models.CharField(max_length=255, blank=True, null=True)
    mail_prof = models.EmailField(max_length=255, blank=True, null=True)
    #BUT 2
    nb_stagaire_but2 = models.IntegerField(blank=True, null=True, default=0)
    nb_alternant_but2 = models.IntegerField(blank=True, null=True, default=0)
    #BUT 3
    nb_stagaire_but3 = models.IntegerField(blank=True, null=True, default=0)
    nb_alternant_but3 = models.IntegerField(blank=True, null=True, default=0)



    def __str__(self):
        return f'Professeur(id={self.id_prof}[num={self.num_prof},civilite={self.civilite_prof},nom={self.nom_prof},prenom={self.prenom_prof},mail={self.mail_prof},nb_stagaire_but2={self.nb_stagaire_but2},nb_alternant_but2={self.nb_alternant_but2},nb_stagaire_but3={self.nb_stagaire_but3},nb_alternant_but3={self.nb_alternant_but3}])'
