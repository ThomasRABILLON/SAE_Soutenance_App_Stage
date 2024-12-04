from django.test import TestCase
from django.utils import timezone

from api.models import Entreprise, TuteurPro, Etudiant, Professeur, Promotion, StageAlt, Salle, Soutenance, DateHoraire

from api.serializers.DateHoraireSerializer import DateHoraireSerializer
from api.serializers.EntrepriseSerializer import EntrepriseSerializer
from api.serializers.EtudiantSerializer import EtudiantSerializer
from api.serializers.ProfesseurSerializer import ProfesseurSerializer
from api.serializers.PromotionSerializer import PromotionSerializer
from api.serializers.SalleSerializer import SalleSerializer
from api.serializers.SoutenanceSerializer import SoutenanceSerializer
from api.serializers.StageAltSerializer import StageAltSerializer
from api.serializers.TuteurProSerializer import TuteurProSerializer

from datetime import timedelta

class SerializersTestCase(TestCase):

    def setUp(self):
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

        self.etudiant = Etudiant.objects.create(
            num_etu="123456",
            ine_etu="INE123456789",
            civilite_etu="Mlle",
            nom_etu="Dupont",
            prenom_etu="Marie",
            mail_etu="marie.dupont@etu.com",
            alternant=True
        )

        self.professeur = Professeur.objects.create(
            num_prof="789012",
            civilite_prof="Mme",
            nom_prof="Martin",
            prenom_prof="Claire",
            mail_prof="c.martin@univ.com"
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
            dt_date_fin_stg_alt=(timezone.now() + timedelta(days=90)).date(),
            duree_stg_alt=90,
            entreprise=self.entreprise,
            tuteur_pro=self.tuteur_pro,
            tuteur_univ=self.professeur,
            etudiant=self.etudiant
        )

        self.salle = Salle.objects.create(
            nom_salle="Salle A"
        )

        self.date_horaire = DateHoraire.objects.create(
            dt_date=timezone.now().date(),
            heure=timezone.now().time(),
            duree=60
        )

        self.soutenance = Soutenance.objects.create(
            stg_alt=self.stage,
            horaire=self.date_horaire,
            salle=self.salle,
            prof_candide=self.professeur
        )

    def test_entreprise_serializer(self):
        serializer = EntrepriseSerializer(self.entreprise)
        data = serializer.data
        self.assertEqual(data['nom_etp'], "TechCorp")
        self.assertEqual(data['cp_etp'], "75001")
        self.assertEqual(data['ville_etp'], "Paris")

    def test_tuteur_pro_serializer(self):
        serializer = TuteurProSerializer(self.tuteur_pro)
        data = serializer.data
        self.assertEqual(data['civilite_tut_pro'], "M.")
        self.assertEqual(data['nom_tut_pro'], "Durand")
        self.assertEqual(data['prenom_tut_pro'], "Jean")
        self.assertEqual(data['tel_tut_pro'], "0102030405")
        self.assertEqual(data['gsm_tut_pro'], "0607080910")
        self.assertEqual(data['mail_tut_pro'], "j.durand@techcorp.com")
        self.assertEqual(data['entreprise'], self.entreprise.id_etp)

    def test_etudiant_serializer(self):
        serializer = EtudiantSerializer(self.etudiant)
        data = serializer.data
        self.assertEqual(data['num_etu'], "123456")
        self.assertEqual(data['ine_etu'], "INE123456789")
        self.assertEqual(data['civilite_etu'], "Mlle")
        self.assertEqual(data['nom_etu'], "Dupont")
        self.assertEqual(data['prenom_etu'], "Marie")
        self.assertEqual(data['mail_etu'], "marie.dupont@etu.com")
        self.assertEqual(data['alternant'], True)

    def test_professeur_serializer(self):
        serializer = ProfesseurSerializer(self.professeur)
        data = serializer.data
        self.assertEqual(data['num_prof'], "789012")
        self.assertEqual(data['civilite_prof'], "Mme")
        self.assertEqual(data['nom_prof'], "Martin")
        self.assertEqual(data['prenom_prof'], "Claire")
        self.assertEqual(data['mail_prof'], "c.martin@univ.com")

    def test_promotion_serializer(self):
        serializer = PromotionSerializer(self.promotion)
        data = serializer.data
        self.assertEqual(data['annee_promo'], 2024)
        self.assertEqual(data['filiere_promo'], "Informatique")

    def test_stage_alt_serializer(self):
        serializer = StageAltSerializer(self.stage)
        data = serializer.data
        self.assertEqual(data['titre_stg_alt'], "Développement Web")
        self.assertEqual(data['theme_stg_alt'], "Full-stack")
        self.assertEqual(data['intitule_env_stg_alt'], "Développement d'une application")
        self.assertEqual(data['dt_date_debut_stg_alt'], str(self.stage.dt_date_debut_stg_alt))
        self.assertEqual(data['dt_date_fin_stg_alt'], str(self.stage.dt_date_fin_stg_alt))
        self.assertEqual(data['duree_stg_alt'], 90)
        self.assertEqual(data['entreprise'], self.entreprise.id_etp)
        self.assertEqual(data['tuteur_pro'], self.tuteur_pro.id_tut_pro)
        self.assertEqual(data['tuteur_univ'], self.professeur.id_prof)
        self.assertEqual(data['etudiant'], self.etudiant.id_etu)

    def test_salle_serializer(self):
        serializer = SalleSerializer(self.salle)
        data = serializer.data
        self.assertEqual(data['nom_salle'], "Salle A")

    def test_date_horaire_serializer(self):
        serializer = DateHoraireSerializer(self.date_horaire)
        data = serializer.data
        self.assertEqual(data['dt_date'], str(self.date_horaire.dt_date))
        self.assertEqual(data['heure'], str(self.date_horaire.heure))
        self.assertEqual(data['duree'], 60)

    def test_soutenance_serializer(self):
        serializer = SoutenanceSerializer(self.soutenance)
        data = serializer.data
        self.assertEqual(data['stg_alt'], self.stage.id_stg_alt)
        self.assertEqual(data['horaire'], self.date_horaire.id_date_horaire)
        self.assertEqual(data['salle'], self.salle.id_salle)
        self.assertEqual(data['prof_candide'], self.professeur.id_prof)