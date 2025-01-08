from django.test import TestCase

from common.services.insert import Insert
from common.services.delete import Delete

from datetime import date, time, timedelta


class ServiceDeleteTestCase(TestCase):

    def setUp(self):
        self.insert = Insert()
        self.insert.insert_entreprise("TechCorp", "75001", "Paris", id_etp=2)
        self.insert.insert_tuteur_pro("M.", "Durand", "Jean", "0102030405", "0607080910", "durand.jean@etp.com", 2, id_tut_pro=2)
        self.insert.insert_professeur("p12345", "Mme", "Martin", "Claire", "martin.claire@prof.com", id_prof=2)
        self.insert.insert_etudiant("12345", "INE123456789", "Mlle", "Dupont", "Marie", "dupont.marie@etu.com", False, id_etu=2)
        self.insert.insert_date_horaire(date.today(), time(1, 0, 0), 120, id_date_horaire=2)
        self.insert.insert_salle("A001", id_salle=2)
        self.insert.insert_stage_alt("Développement Web", "Développement d'une application Web", "intitule", date.today(), date.today() + timedelta(days=30), 30, 2, 2, 2, 2, id_stg_alt=2)
        self.delete = Delete()
        
    def test_delete_entreprise(self):
        self.assertTrue(self.delete.delete_entreprise(2))
        self.assertFalse(self.delete.delete_entreprise(2))
        
    def test_delete_tuteur_pro(self):
        self.assertTrue(self.delete.delete_tuteur_pro(2))
        self.assertFalse(self.delete.delete_tuteur_pro(2))
    
    def test_delete_professeur(self):
        self.assertTrue(self.delete.delete_professeur(2))
        self.assertFalse(self.delete.delete_professeur(2))
    
    def test_delete_etudiant(self):
        self.assertTrue(self.delete.delete_etudiant(2))
        self.assertFalse(self.delete.delete_etudiant(2))
    
    def test_delete_date_horaire(self):
        self.assertTrue(self.delete.delete_date_horaire(2))
        self.assertFalse(self.delete.delete_date_horaire(2))
    
    def test_delete_salle(self):
        self.assertTrue(self.delete.delete_salle(2))
        self.assertFalse(self.delete.delete_salle(2))
    
    def test_delete_stage_alt(self):
        self.assertTrue(self.delete.delete_stage_alt(2))
        self.assertFalse(self.delete.delete_stage_alt(2))