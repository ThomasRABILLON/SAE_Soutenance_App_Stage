from django.test import TestCase
from django.utils import timezone

from datetime import timedelta

from common.models.Entreprise import Entreprise
from common.models.TuteurPro import TuteurPro
from common.models.Professeur import Professeur
from common.models.Etudiant import Etudiant
from common.models.Promotion import Promotion
from common.models.StageAlt import StageAlt
from common.models.Salle import Salle
from common.models.DateHoraire import DateHoraire
from common.models.Soutenance import Soutenance

class ModelsTestCase(TestCase):

    def setUp(self):
        # Création des instances de base pour les tests
        self.entreprise = Entreprise.objects.create(
            nom_etp="TechCorp",
            cp_etp="75001",
            ville_etp="Paris"
        )

        self.tuteur_pro = TuteurPro.objects.create(
            civilite_tut_pro="M.",
            nom_tut_pro="Durand",
            prenom_tut_pro="Jean",
            tel_tut_pro="0102030405",
            gsm_tut_pro="0607080910",
            mail_tut_pro="j.durand@techcorp.com",
            entreprise=self.entreprise
        )

        self.professeur = Professeur.objects.create(
            num_prof="p12345",
            civilite_prof="Mme",
            nom_prof="Martin",
            prenom_prof="Claire",
            mail_prof="c.martin@univ.com"
        )

        self.etudiant = Etudiant.objects.create(
            num_etu="12345",
            ine_etu="INE123456789",
            civilite_etu="Mlle",
            nom_etu="Dupont",
            prenom_etu="Marie",
            mail_etu="marie.dupont@etu.com",
            alternant=False
        )

        self.promotion = Promotion.objects.create(
            annee_promo=2024,
            filiere_promo="Informatique"
        )

        self.stage = StageAlt.objects.create(
            titre_stg_alt="Développement Web",
            theme_stg_alt="Full-stack",
            intitule_env_stg_alt="Développement d'une application",
            dt_date_debut_stg_alt=timezone.now().date(),
            dt_date_fin_stg_alt=timezone.now().date() + timedelta(days=90),
            duree_stg_alt=90,
            entreprise=self.entreprise,
            tuteur_pro=self.tuteur_pro,
            tuteur_univ=self.professeur,
            etudiant=self.etudiant
        )

        self.salle = Salle.objects.create(nom_salle="Salle A")

        self.date_horaire = DateHoraire.objects.create(
            dt_date=timezone.now().date(),
            heure=timezone.now().time(),
            duree=120
        )

        self.soutenance = Soutenance.objects.create(
            stg_alt=self.stage,
            horaire=self.date_horaire,
            salle=self.salle,
            prof_candide=self.professeur
        )

    def test_entreprise_creation(self):
        self.assertEqual(str(self.entreprise), 'Entreprise(id=0[nom=TechCorp,[cp=75001,ville=Paris]])')

    def test_tuteur_creation(self):
        self.assertEqual(str(self.tuteur_pro), f'TuteurPro(id=0[civilite=M.,nom=Durand,prenom=Jean,tel=0102030405,gsm=0607080910,mail=j.durand@techcorp.com,entreprise={self.entreprise}])')

    def test_etudiant_creation(self):
        self.assertEqual(str(self.etudiant), 'Etudiant(id=0[ine=INE123456789,[civilite=Mlle,nom=Dupont,prenom=Marie,mail=marie.dupont@etu.com,alternant=False]])')

    def test_professeur_creation(self):
        self.assertEqual(str(self.professeur), 'Professeur(id=0[num=p12345,civilite=Mme,nom=Martin,prenom=Claire,mail=c.martin@univ.com])')

    def test_promotion_creation(self):
        self.assertEqual(str(self.promotion), 'Promotion(id=0[annee=2024,filiere=Informatique])')

    def test_stage_creation(self):
        self.assertEqual(
            str(self.stage),
            f'StageAlt(id=0[titre=Développement Web,theme=Full-stack,intitule_env=Développement d\'une application, [date_debut={self.stage.dt_date_debut_stg_alt},date_fin={self.stage.dt_date_fin_stg_alt},duree={self.stage.duree_stg_alt}], entreprise={self.entreprise},tuteur_pro={self.tuteur_pro},tuteur_univ={self.professeur},etudiant={self.etudiant}])'
        )

    def test_salle_creation(self):
        self.assertEqual(str(self.salle), 'Salle(id=0[nom=Salle A])')

    def test_date_horaire_creation(self):
        self.assertEqual(
            str(self.date_horaire),
            f'DateHoraire(id=0[date={self.date_horaire.dt_date},heure={self.date_horaire.heure},duree={self.date_horaire.duree}])'
        )

    def test_soutenance_creation(self):
        self.assertEqual(
            str(self.soutenance),
            f'Soutenance(id=0[stg={self.stage}, hor={self.date_horaire}, salle={self.salle}, prof={self.professeur}])'
        )

    def test_relations(self):
        self.assertEqual(self.stage.entreprise, self.entreprise)
        self.assertEqual(self.stage.tuteur_pro, self.tuteur_pro)
        self.assertEqual(self.soutenance.stg_alt, self.stage)