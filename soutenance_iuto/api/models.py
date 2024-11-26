from django.db import models

# Create your models here.
class Entreprise(models.Model):
    class Meta:
        verbose_name = "Entreprise"

    id_etp = models.AutoField(primary_key=True)
    nom_etp = models.CharField(max_length=255, blank=True, null=True)
    cp_etp = models.CharField(max_length=255, blank=True, null=True)
    ville_etp = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.id_etp}[{self.nom_etp},[{self.cp_etp},{self.ville_etp}]]'

class TuteurPro(models.Model):
    class Meta:
        verbose_name = "TuteurPro"

    id_tut_pro = models.AutoField(primary_key=True)
    civilite_tut_pro = models.CharField(max_length=255, blank=True, null=True)
    nom_tut_pro = models.CharField(max_length=255, blank=True, null=True)
    prenom_tut_pro = models.CharField(max_length=255, blank=True, null=True)
    tel_tut_pro = models.CharField(max_length=10, blank=True, null=True)
    gsm_tut_pro = models.CharField(max_length=10, blank=True, null=True)
    mail_tut_pro = models.EmailField(max_length=255, blank=True, null=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id_tut_pro}[{self.civilite_tut_pro},{self.nom_tut_pro},{self.prenom_tut_pro},[{self.tel_tut_pro},{self.gsm_tut_pro}],{self.mail_tut_pro}]'

class Etudiant(models.Model):
    class Meta:
        verbose_name = "Etudiant"
    
    id_etu = models.AutoField(primary_key=True)
    ine_etu = models.CharField(max_length=255, blank=True, null=True)
    civilite_etu = models.CharField(max_length=255, blank=True, null=True)
    nom_etu = models.CharField(max_length=255, blank=True, null=True)
    prenom_etu = models.CharField(max_length=255, blank=True, null=True)
    mail_etu = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.id_etu}[{self.ine_etu},[{self.civilite_etu},{self.nom_etu},{self.prenom_etu},{self.mail_etu}]]'

class Professeur(models.Model):
    class Meta:
        verbose_name = "Professeur"

    id_prof = models.AutoField(primary_key=True)
    civilite_prof = models.CharField(max_length=255, blank=True, null=True)
    nom_prof = models.CharField(max_length=255, blank=True, null=True)
    prenom_prof = models.CharField(max_length=255, blank=True, null=True)
    mail_prof = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.id_prof}[{self.civilite_prof},{self.nom_prof},{self.prenom_prof},{self.mail_prof}]'

class Promotion(models.Model):
    class Meta:
        verbose_name = "Promotion"

    id_promo = models.AutoField(primary_key=True)
    annee_promo = models.IntegerField()
    filiere_promo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.id_promo}[{self.annee_promo},{self.filiere_promo}]'

class EstDansPromotion(models.Model):
    class Meta:
        verbose_name = "EstDansPromotion"

    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.etudiant} -> {self.promotion}'

class EstResponsable(models.Model):
    class Meta:
        verbose_name = "EstResponsable"

    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.professeur} -> {self.promotion}'
    
class StageAlt(models.Model):
    class Meta:
        verbose_name = "StageAlt"

    id_stg_alt = models.AutoField(primary_key=True)
    titre_stg_alt = models.CharField(max_length=255, blank=True, null=True)
    theme_stg_alt = models.CharField(max_length=255, blank=True, null=True)
    intitule_env_stg_alt = models.CharField(max_length=255, blank=True, null=True)
    dt_date_debut_stg_alt = models.DateField()
    dt_date_fin_stg_alt = models.DateField()
    duree_stg_alt = models.IntegerField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    tuteur_pro = models.ForeignKey(TuteurPro, on_delete=models.CASCADE)
    tuteur_univ = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_stg_alt}[{self.titre_stg_alt},{self.theme_stg_alt},{self.intitule_env_stg_alt}[{self.dt_date_debut_stg_alt},{self.dt_date_fin_stg_alt},{self.duree_stg_alt}]]'
    
class Salle(models.Model):
    class Meta:
        verbose_name = "Salle"

    id_salle = models.AutoField(primary_key=True)
    nom_salle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.id_salle}[{self.nom_salle}]'
    
class DateHoraire(models.Model):
    class Meta:
        verbose_name = "DateHoraire"

    id_date_horaire = models.AutoField(primary_key=True)
    dt_date = models.DateField()
    heure = models.TimeField()
    duree = models.IntegerField()

    def __str__(self):
        return f'{self.id_date_horaire}[{self.dt_date},{self.heure},{self.heure}]'
    
class Soutenance(models.Model):
    class Meta:
        verbose_name = "Soutenance"

    id_sout = models.AutoField(primary_key=True)
    stg_alt = models.ForeignKey(StageAlt, on_delete=models.CASCADE)
    horaire = models.ForeignKey(DateHoraire, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    prof_candide = models.ForeignKey(Professeur, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_sout}[{self.salle},{self.date_horaire},{self.stage_alt}]'
