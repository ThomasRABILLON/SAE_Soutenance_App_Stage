from django.test import TestCase
from api.models import (
    Entreprise, TuteurPro, Etudiant, Professeur, Promotion,
    EstDansPromotion, EstResponsable, StageAlt, Salle, DateHoraire,
    Soutenance, InscriptionSoutenance, InscriptionSuivi, Secretaire
)
from django.utils import timezone
from datetime import timedelta

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
            alternant=True
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
        self.assertEqual(str(self.entreprise), "0[TechCorp,[75001,Paris]]")

    def test_tuteur_creation(self):
        self.assertEqual(str(self.tuteur_pro), "0[M.,Durand,Jean,[0102030405,0607080910],j.durand@techcorp.com]")

    def test_etudiant_creation(self):
        self.assertEqual(str(self.etudiant), "0[INE123456789,[Mlle,Dupont,Marie,marie.dupont@etu.com]]")

    def test_professeur_creation(self):
        self.assertEqual(str(self.professeur), "0[Mme,Martin,Claire,c.martin@univ.com]")

    def test_promotion_creation(self):
        self.assertEqual(str(self.promotion), "0[2024,Informatique]")

    def test_stage_creation(self):
        self.assertEqual(
            str(self.stage),
            f"0[Développement Web,Full-stack,Développement d'une application[{self.stage.dt_date_debut_stg_alt},{self.stage.dt_date_fin_stg_alt},90]]"
        )

    def test_salle_creation(self):
        self.assertEqual(str(self.salle), "0[Salle A]")

    def test_date_horaire_creation(self):
        self.assertEqual(
            str(self.date_horaire),
            f"0[{self.date_horaire.dt_date},{self.date_horaire.heure},{self.date_horaire.heure}]"
        )

    def test_soutenance_creation(self):
        self.assertEqual(
            str(self.soutenance),
            f"0[{self.salle},{self.date_horaire},{self.stage}]"
        )

    def test_relations(self):
        self.assertEqual(self.stage.entreprise, self.entreprise)
        self.assertEqual(self.stage.tuteur_pro, self.tuteur_pro)
        self.assertEqual(self.soutenance.stg_alt, self.stage)
