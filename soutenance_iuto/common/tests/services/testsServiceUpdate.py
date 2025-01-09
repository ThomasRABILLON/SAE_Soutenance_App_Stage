from django.test import TestCase

from common.services.update import Update
from common.services.insert import Insert
from common.models.DateHoraire import DateHoraire
from common.models.Entreprise import Entreprise
from common.models.Etudiant import Etudiant
from common.models.Professeur import Professeur
from common.models.TuteurPro import TuteurPro
from common.models.StageAlt import StageAlt


from datetime import date, time, timedelta


class ServiceUpdateTesCase(TestCase):

    def setUp(self):
        self.insert = Insert()

        self.insert.insert_entreprise("TechCorp", "75001", "Paris", id_etp=2)
        self.insert.insert_tuteur_pro("M.", "Durand", "Jean", "0102030405", "0607080910", "durand.jean@etp.com", 2, id_tut_pro=2)
        self.insert.insert_professeur("p12345", "Mme", "Martin", "Claire", "martin.claire@prof.com", id_prof=2)
        self.insert.insert_etudiant("12345", "INE123456789", "Mlle", "Dupont", "Marie", "dupont.marie@etu.com", False, id_etu=2)
        self.insert.insert_date_horaire(date.today(), time(1, 0, 0), 120, id_date_horaire=2)
        self.insert.insert_salle("A001", id_salle=2)
        self.insert.insert_stage_alt("Développement Web", "Développement d'une application Web", "intitule", date.today(), date.today() + timedelta(days=30), 30, 2, 2, 2, 2, id_stg_alt=2)
        self.update = Update()

    def test_update_entreprise(self):
        entreprise = Entreprise.query.get(2)
        entreprise.nom = "TechCorp"
        self.assertTrue(self.update.update_entreprise(entreprise))
        self.assertEqual(Entreprise.query.get(2).nom, "TechCorp")

    def test_update_teuteur_pro(self):
        tuteur_pro = TuteurPro.query.get(2)
        tuteur_pro.nom = "Durand"
        self.assertTrue(self.update.update_tuteur_pro(tuteur_pro))
        self.assertEqual(TuteurPro.query.get(2).nom, "Durand")

    def test_update_professeur(self):
        professeur = Professeur.query.get(2)
        professeur.nom = "Martin"
        self.assertTrue(self.update.update_professeur(professeur))
        self.assertEqual(Professeur.query.get(2).nom, "Martin")
    
    def test_update_etudiant(self):
        etudiant = Etudiant.query.get(2)
        etudiant.nom = "Dupont"
        self.assertTrue(self.update.update_etudiant(etudiant))
        self.assertEqual(Etudiant.query.get(2).nom, "Dupont")

    def test_update_date_horaire(self):
        date_horaire = DateHoraire.query.get(2)
        date_horaire.date = date.today() + timedelta(days=1)
        self.assertTrue(self.update.update_date_horaire(date_horaire))
        self.assertEqual(DateHoraire.query.get(2).date, date.today() + timedelta(days=1))
        
    def test_update_stage_alt(self):
        stage_alt = StageAlt.query.get(2)
        stage_alt.intitule = "Développement Web"
        self.assertTrue(self.update.update_stage_alt(stage_alt))
        self.assertEqual(StageAlt.query.get(2).intitule, "Développement Web")