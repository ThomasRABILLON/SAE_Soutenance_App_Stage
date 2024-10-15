from django.db import models

# Create your models here.

class AppStagiaire(models.Model):
    class Meta:
        verbose_name = "AppStagiaire"

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE)
    entreprise = models.ForeignKey('Entreprise', on_delete=models.CASCADE)
    tuteur_pro = models.ForeignKey('TuteurPro', on_delete=models.CASCADE)
    tuteur_univ = models.ForeignKey('Professeur', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + ' ' + self.prenom

class Entreprise(models.Model):
    class Meta:
        verbose_name = "Entreprise"

    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nom

class Professeur(models.Model):
    class Meta:
        verbose_name = "Professeur"

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nom + ' ' + self.prenom
    
class Promotion(models.Model):
    class Meta:
        verbose_name = "Promotion"

    nom = models.CharField(max_length=255)
    annee = models.IntegerField()
    responsable = models.ForeignKey('Professeur', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + ' ' + str(self.annee)

class Salle(models.Model):
    class Meta:
        verbose_name = "Salle"

    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    
class Secretaire(models.Model):
    class Meta:
        verbose_name = "Secretaire"

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nom + ' ' + self.prenom

class TuteurPro(models.Model):
    class Meta:
        verbose_name = "TuteurPro"

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    entreprise = models.ForeignKey('Entreprise', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + ' ' + self.prenom
    
class Soutenance(models.Model):
    class Meta:
        verbose_name = "Soutenance"

    date = models.DateField()
    heure = models.TimeField()
    salle = models.ForeignKey('Salle', on_delete=models.CASCADE)
    app_stage = models.ForeignKey('AppStagiaire', on_delete=models.CASCADE)
    tuteur_pro = models.ForeignKey('TuteurPro', on_delete=models.CASCADE)
    tuteur_univ = models.ForeignKey('Professeur', on_delete=models.CASCADE)
    prof_candide = models.ForeignKey('Professeur', on_delete=models.CASCADE)

    def __str__(self):
        return self.app_stage.nom + ' ' + self.app_stage.prenom + ' ' + str(self.date) + ' ' + str(self.heure)
