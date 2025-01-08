from django.test import TestCase

from common.services.insert import Insert

from datetime import date, time, timedelta


class ServiceInsertTestCase(TestCase):

    def setUp(self):
        self.insert = Insert()
        self.insert.insert_entreprise("TechCorp", "75001", "Paris", id_etp=2)
        self.insert.insert_tuteur_pro(
            "M.",
            "Durand",
            "Jean",
            "0102030405",
            "0607080910",
            "durand.jean@etp.com",
            2,
            id_tut_pro=2,
        )
        self.insert.insert_professeur(
            "p12345", "Mme", "Martin", "Claire", "martin.claire@prof.com", id_prof=2
        )
        self.insert.insert_etudiant(
            "12345",
            "INE123456789",
            "Mlle",
            "Dupont",
            "Marie",
            "dupont.marie@etu.com",
            False,
            id_etu=2,
        )
        self.insert.insert_date_horaire(
            date.today(), time(1, 0, 0), 120, id_date_horaire=2
        )
        self.insert.insert_salle("A001", id_salle=2)
        self.insert.insert_stage_alt(
            "Développement Web",
            "Développement d'une application Web",
            "intitule",
            date.today(),
            date.today() + timedelta(days=30),
            30,
            2,
            2,
            2,
            2,
            id_stg_alt=2,
        )

    def test_insert_entreprise(self):
        self.assertTrue(
            self.insert.insert_entreprise("TechCorp", "75001", "Paris", id_etp=1)
        )
        self.assertFalse(
            self.insert.insert_entreprise("TechCorp", "75001", "Paris", id_etp=1)
        )

    def test_insert_tuteur_pro(self):
        self.assertTrue(
            self.insert.insert_tuteur_pro(
                "M.",
                "Durand",
                "Jean",
                "0102030405",
                "0607080910",
                "durand.jean@etp.com",
                2,
                id_tut_pro=1,
            )
        )
        self.assertFalse(
            self.insert.insert_tuteur_pro(
                "Mme",
                "Durand",
                "Jeanne",
                "0110203040",
                "0655070809",
                "durand.jeanne@etp.com",
                2,
                id_tut_pro=1,
            )
        )

    def test_insert_professeur(self):
        self.assertTrue(
            self.insert.insert_professeur(
                "p12345", "Mme", "Martin", "Claire", "martin.claire@prof.com", id_prof=1
            )
        )
        self.assertFalse(
            self.insert.insert_professeur(
                "p12345", "Mme", "Martin", "Claire", "martin.claire@prof.com", id_prof=1
            )
        )

    def test_insert_etudiant(self):
        self.assertTrue(
            self.insert.insert_etudiant(
                "12345",
                "INE123456789",
                "Mlle",
                "Dupont",
                "Marie",
                "dupont.marie@etu.com",
                False,
                id_etu=1,
            )
        )
        self.assertFalse(
            self.insert.insert_etudiant(
                "12345",
                "INE123456789",
                "Mlle",
                "Dupont",
                "Marie",
                "dupont.marie@etu.com",
                False,
                id_etu=1,
            )
        )

    def test_insert_promotion(self):
        self.assertTrue(self.insert.insert_promotion(2024, "Informatique", id_promo=1))
        self.assertFalse(self.insert.insert_promotion(2023, "Informatique", id_promo=1))

    def test_insert_stage_alt(self):
        self.assertTrue(
            self.insert.insert_stage_alt(
                "Développement Web",
                "Développement d'une application Web",
                "intitule",
                date.today(),
                date.today() + timedelta(days=30),
                30,
                2,
                2,
                2,
                2,
                id_stg_alt=1,
            )
        )
        self.assertFalse(
            self.insert.insert_stage_alt(
                "Développement Multimedia",
                "Développement d'une application Multimedia",
                date.today(),
                date.today() + timedelta(days=30),
                30,
                2,
                2,
                2,
                2,
                2,
                id_stg_alt=1,
            )
        )

    def test_insert_salle(self):
        self.assertTrue(self.insert.insert_salle("A001", id_salle=1))
        self.assertFalse(self.insert.insert_salle("A002", id_salle=1))

    def test_insert_date_horaire(self):
        self.assertTrue(
            self.insert.insert_date_horaire(
                date.today(), time(1, 0, 0), 120, id_date_horaire=1
            )
        )
        self.assertFalse(
            self.insert.insert_date_horaire(
                date.today() + timedelta(days=1), time(1, 0, 0), 120, id_date_horaire=1
            )
        )

    def test_insert_soutenance(self):
        self.assertTrue(self.insert.insert_soutenance(2, 2, 2, 2, id_soutenance=1))
        self.assertTrue(self.insert.insert_soutenance(2, 2, 2, 2, id_soutenance=2))
        self.assertFalse(self.insert.insert_soutenance(2, 2, 2, 2, id_soutenance=1))
