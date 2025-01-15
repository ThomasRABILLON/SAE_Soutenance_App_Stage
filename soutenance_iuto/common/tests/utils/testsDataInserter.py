from django.test import TestCase

from common.services.get import Get, GetAll, GetById
from common.utils.ExternalDataInserter import ExternalDataInserter

from datetime import date

class testsDataInserter(TestCase):
    def setUp(self):
        pass
    
    def test_alternants_from_csv(self):
        ExternalDataInserter.alternants_from_csv('../data_test/alternant/Alternant - BUT3 Sujet.csv')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').nom_etu, 'ABADA')
        self.assertEqual(Get.get_promotion_by_annee_filiere(2024, 'BUT3').filiere_promo, 'BUT3')
        self.assertEqual(GetAll.get_all_promotion().count(), 1)
        self.assertEqual(GetById.get_est_dans_promotion_by_etu_id(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').id_etu).first().etudiant.nom_etu, 'ABADA')
        self.assertEqual(GetById.get_est_dans_promotion_by_etu_id(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').id_etu).first().promotion.filiere_promo, 'BUT3')
        self.assertEqual(Get.get_professeur_by_nom_prenom('Christophe', 'Léchopier').nom_prof, 'Christophe')
        self.assertEqual(Get.get_entreprise_by_nom('STMICROELECTRONICS TOURS').nom_etp, 'STMICROELECTRONICS TOURS')
        self.assertEqual(Get.get_tuteur_pro_by_nom('DEVOYON').nom_tut_pro, 'DEVOYON')
        self.assertEqual(Get.get_tuteur_pro_by_nom('DEVOYON').civilite_tut_pro, 'Monsieur')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').id_etu).first().etudiant.nom_etu, 'ABADA')
        
    def test_alternants_from_excel(self):
        ExternalDataInserter.alternants_from_excel('../data_test/alternant/Alternant.xlsx')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').nom_etu, 'ABADA')
        self.assertEqual(Get.get_promotion_by_annee_filiere(2024, 'BUT3').filiere_promo, 'BUT3')
        self.assertEqual(GetAll.get_all_promotion().count(), 1)
        self.assertEqual(GetById.get_est_dans_promotion_by_etu_id(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').id_etu).first().etudiant.nom_etu, 'ABADA')
        self.assertEqual(GetById.get_est_dans_promotion_by_etu_id(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').id_etu).first().promotion.filiere_promo, 'BUT3')
        self.assertEqual(Get.get_professeur_by_nom_prenom('Christophe', 'Léchopier').nom_prof, 'Christophe')
        self.assertEqual(Get.get_entreprise_by_nom('STMICROELECTRONICS TOURS').nom_etp, 'STMICROELECTRONICS TOURS')
        self.assertEqual(Get.get_tuteur_pro_by_nom('DEVOYON').nom_tut_pro, 'DEVOYON')
        self.assertEqual(Get.get_tuteur_pro_by_nom('DEVOYON').civilite_tut_pro, 'Monsieur')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('ABADA', 'Khalil').id_etu).first().etudiant.nom_etu, 'ABADA')
    
    def test_stagiaires_from_csv(self):
        ExternalDataInserter.stagiaires_from_csv('../data_test/stagiaire/tableur stages 2023 2024 extraction AREXIS.xls - Extraction.csv')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').nom_etu, 'BABA')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').ine_etu, '')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').civilite_etu, 'M.')
        self.assertEqual(Get.get_entreprise_by_nom('LIFO').nom_etp, 'LIFO')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').nom_tut_pro, 'DUBOIS')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').prenom_tut_pro, 'Aurélie')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').civilite_tut_pro, 'Mme')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').tel_tut_pro, '02 36 17 46 75')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').gsm_tut_pro, '')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').mail_tut_pro, 'aurelie.dubois@developpement-durable.gouv.fr')
        
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().etudiant.nom_etu, 'BABA')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().entreprise.nom_etp, 'DREAL CENTRE-VAL DE LOIRE/SMT/DTRV/UAPGE')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.nom_tut_pro, 'DUBOIS')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.prenom_tut_pro, 'Aurélie')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.civilite_tut_pro, 'Mme')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.tel_tut_pro, '02 36 17 46 75')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.gsm_tut_pro, '')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.mail_tut_pro, 'aurelie.dubois@developpement-durable.gouv.fr')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().tuteur_univ, None)
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().titre_stg_alt, 'Intégrer l\'équipe de développement du groupe Partnaire, répondre aux enjeu de mise en place de brique d\'IA par le développement d\'un démonstrateur')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BLIN', 'PIERRE').id_etu).first().theme_stg_alt, 'Transformation SharePoint, Power Automate')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().intitule_env_stg_alt, '')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().dt_date_debut_stg_alt, date.fromisoformat('2024-04-22'))
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().dt_date_fin_stg_alt, date.fromisoformat('2024-06-14'))
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().duree_stg_alt, 8)
    
    def test_stagiaires_from_excel(self):
        ExternalDataInserter.stagiaires_from_excel('../data_test/stagiaire/tableur stages 2023 2024 extraction AREXIS.xls')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').nom_etu, 'BABA')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').ine_etu, '')
        self.assertEqual(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').civilite_etu, 'M.')
        self.assertEqual(Get.get_entreprise_by_nom('LIFO').nom_etp, 'LIFO')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').nom_tut_pro, 'DUBOIS')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').prenom_tut_pro, 'Aurélie')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').civilite_tut_pro, 'Mme')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').tel_tut_pro, '02 36 17 46 75')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').gsm_tut_pro, '')
        self.assertEqual(Get.get_tuteur_pro_by_nom_prenom('DUBOIS', 'Aurélie').mail_tut_pro, 'aurelie.dubois@developpement-durable.gouv.fr')
        
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().etudiant.nom_etu, 'BABA')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().entreprise.nom_etp, 'DREAL CENTRE-VAL DE LOIRE/SMT/DTRV/UAPGE')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.nom_tut_pro, 'DUBOIS')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.prenom_tut_pro, 'Aurélie')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.civilite_tut_pro, 'Mme')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.tel_tut_pro, '02 36 17 46 75')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.gsm_tut_pro, '')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BABA', 'AHMET').id_etu).first().tuteur_pro.mail_tut_pro, 'aurelie.dubois@developpement-durable.gouv.fr')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().tuteur_univ, None)
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().titre_stg_alt, 'Intégrer l\'équipe de développement du groupe Partnaire, répondre aux enjeu de mise en place de brique d\'IA par le développement d\'un démonstrateur')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BLIN', 'PIERRE').id_etu).first().theme_stg_alt, 'Transformation SharePoint, Power Automate')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().intitule_env_stg_alt, '')
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().dt_date_debut_stg_alt, date.fromisoformat('2024-04-22'))
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().dt_date_fin_stg_alt, date.fromisoformat('2024-06-14'))
        self.assertEqual(Get.get_stage_alt_by_etu_id(Get.get_etudiant_by_nom_prenom('BARACHE', 'YANNIS').id_etu).first().duree_stg_alt, 8)
        