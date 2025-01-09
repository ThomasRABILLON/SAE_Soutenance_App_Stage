import pandas as pd

from common.services.insert import Insert
from common.services.get import Get

from datetime import date


class ExternalDataInserter:
    @staticmethod
    def alternants_from_csv(csv_path: str) -> None:
        # Lire le fichier CSV
        alternants_df = pd.read_csv(csv_path, sep=',')
        
        # Renommer les colonnes nommées 'CP ET VILLE_ENTREPRISE' en 'CP_ENTREPRISE' et 'NOM_MA' en 'CIVILITE_MA'
        alternants_df.rename(columns={'CP ET VILLE_ENTREPRISE': 'CP_ENTREPRISE', 'NOM MA': 'CIVILITE_MA'}, inplace=True)
        # Renommer les colonnes 0, 6 et 8 en 'PROMOTION', 'VILLE_ENTREPRISE' et 'NOM_MA'
        alternants_df.rename(columns={'Unnamed: 0': 'PROMOTION', 'Unnamed: 6': 'VILLE_ENTREPRISE', 'Unnamed: 8': 'NOM_MA'}, inplace=True)
        
        for _, row in alternants_df.iterrows():
            Insert.insert_etudiant(str(row['NOM']).strip(), str(row['PRENOM']).strip(), True, id_etu=Get.get_etudiant_last_id() + 1)
            
            if Get.get_promotion_by_annee_filiere(2024, str(row['PROMOTION']).strip()) is None:
                Insert.insert_promotion(2024, str(row['PROMOTION']).strip(), id_promo=Get.get_promotion_last_id() + 1)
            Insert.insert_est_dans_promotion(Get.get_etudiant_by_nom_prenom(str(row['NOM']).strip(), str(row['PRENOM']).strip()).id_etu, Get.get_promotion_by_annee_filiere(2024, str(row['PROMOTION']).strip()).id_promo)
            
            if Get.get_professeur_by_nom_prenom(str(row['TUTEUR']).strip().split(' ')[0], str(row['TUTEUR']).strip().split(' ')[1]) is None:
                Insert.insert_professeur(str(row['TUTEUR']).strip().split(' ')[0], str(row['TUTEUR']).strip().split(' ')[1], id_prof=Get.get_professeur_last_id() + 1)
            
            if Get.get_entreprise_by_nom(str(row['ENTREPRISE']).strip()) is None:
                Insert.insert_entreprise(str(row['ENTREPRISE']).strip(), str(row['VILLE_ENTREPRISE']).strip(), str(row['CP_ENTREPRISE']).strip(), id_etp=Get.get_entreprise_last_id() + 1)
                
            if Get.get_tuteur_pro_by_nom(str(row['NOM_MA']).strip()) is None:
                Insert.insert_tuteur_pro(str(row['NOM_MA']).strip(), prenom="", id_etp=Get.get_entreprise_by_nom(str(row['ENTREPRISE']).strip()).id_etp, civilite=str(row['CIVILITE_MA']).strip(), id_tut_pro=Get.get_tuteur_pro_last_id() + 1)
                
            Insert.insert_stage_alt(Get.get_entreprise_by_nom(str(row['ENTREPRISE']).strip()).id_etp, Get.get_tuteur_pro_by_nom(str(row['NOM_MA']).strip()).id_tut_pro, Get.get_professeur_by_nom_prenom(str(row['TUTEUR']).strip().split(' ')[0], str(row['TUTEUR']).strip().split(' ')[1]).id_prof, Get.get_etudiant_by_nom_prenom(str(row['NOM']).strip(), str(row['PRENOM']).strip()).id_etu, id_stg_alt=Get.get_stg_alt_last_id() + 1)
    
    @staticmethod
    def alternants_from_excel(excel_path: str) -> None:
        # Lire le fichier Excel
        alternants_df = pd.read_excel(excel_path)
        
        # Renommer les colonnes nommées 'CP ET VILLE_ENTREPRISE' en 'CP_ENTREPRISE' et 'NOM_MA' en 'CIVILITE_MA'
        alternants_df.rename(columns={'CP ET VILLE_ENTREPRISE': 'CP_ENTREPRISE', 'NOM MA': 'CIVILITE_MA'}, inplace=True)
        # Renommer les colonnes 0, 6 et 8 en 'PROMOTION', 'VILLE_ENTREPRISE' et 'NOM_MA'
        alternants_df.rename(columns={'Unnamed: 0': 'PROMOTION', 'Unnamed: 6': 'VILLE_ENTREPRISE', 'Unnamed: 8': 'NOM_MA'}, inplace=True)
        
        for _, row in alternants_df.iterrows():
            Insert.insert_etudiant(str(row['NOM']).strip(), str(row['PRENOM']).strip(), True, id_etu=Get.get_etudiant_last_id() + 1)
            
            if Get.get_promotion_by_annee_filiere(2024, str(row['PROMOTION']).strip()) is None:
                Insert.insert_promotion(2024, str(row['PROMOTION']).strip(), id_promo=Get.get_promotion_last_id() + 1)
            Insert.insert_est_dans_promotion(Get.get_etudiant_by_nom_prenom(str(row['NOM']).strip(), str(row['PRENOM']).strip()).id_etu, Get.get_promotion_by_annee_filiere(2024, str(row['PROMOTION']).strip()).id_promo)
            
            if Get.get_professeur_by_nom_prenom(str(row['TUTEUR']).strip().split(' ')[0], str(row['TUTEUR']).strip().split(' ')[1]) is None:
                Insert.insert_professeur(str(row['TUTEUR']).strip().split(' ')[0], str(row['TUTEUR']).strip().split(' ')[1], id_prof=Get.get_professeur_last_id() + 1)
            
            if Get.get_entreprise_by_nom(str(row['ENTREPRISE']).strip()) is None:
                Insert.insert_entreprise(str(row['ENTREPRISE']).strip(), str(row['VILLE_ENTREPRISE']).strip(), str(row['CP_ENTREPRISE']).strip(), id_etp=Get.get_entreprise_last_id() + 1)
                
            if Get.get_tuteur_pro_by_nom(str(row['NOM_MA']).strip()) is None:
                Insert.insert_tuteur_pro(str(row['NOM_MA']).strip(), prenom="", id_etp=Get.get_entreprise_by_nom(str(row['ENTREPRISE']).strip()).id_etp, civilite=str(row['CIVILITE_MA']).strip(), id_tut_pro=Get.get_tuteur_pro_last_id() + 1)

            Insert.insert_stage_alt(Get.get_entreprise_by_nom(str(row['ENTREPRISE']).strip()).id_etp, Get.get_tuteur_pro_by_nom(str(row['NOM_MA']).strip()).id_tut_pro, Get.get_professeur_by_nom_prenom(str(row['TUTEUR']).strip().split(' ')[0], str(row['TUTEUR']).strip().split(' ')[1]).id_prof, Get.get_etudiant_by_nom_prenom(str(row['NOM']).strip(), str(row['PRENOM']).strip()).id_etu, id_stg_alt=Get.get_stg_alt_last_id() + 1)
    
    @staticmethod
    def stagiaires_from_csv(csv_path: str) -> None:
        # Lire le fichier CSV
        stagiaires_df = pd.read_csv(csv_path, sep=',')
        
        # Remplacer les nan par des chaînes vides
        stagiaires_df.fillna('', inplace=True)
        
        # Mettre le type de la colonne 'duree' en str
        stagiaires_df['duree'] = stagiaires_df['duree'].astype(str)
        
        for _, row in stagiaires_df.iterrows():
            if Get.get_etudiant_by_nom_prenom(str(row['nom_stagiaire']).strip(), str(row['prenom_stagaire']).strip()) is None:
                Insert.insert_etudiant(str(row['nom_stagiaire']).strip(), str(row['prenom_stagaire']).strip(), False, num=str(row['ine']).strip(),civilite=str(row['civilite_stagiaire']).strip(), id_etu=Get.get_etudiant_last_id() + 1)
                
            if Get.get_entreprise_by_nom(str(row['service_adm_nom_service']).strip()) is None:
                Insert.insert_entreprise(str(row['service_adm_nom_service']).strip(), str(row['service_adm_ville_service']).strip(), str(row['service_adm_cp_service']).strip(), id_etp=Get.get_entreprise_last_id() + 1)
                
            if Get.get_tuteur_pro_by_nom_prenom(str(row['nom_employe_tut']).strip(), str(row['prenom_employe_tut']).strip()) is None:
                Insert.insert_tuteur_pro(str(row['nom_employe_tut']).strip(), str(row['prenom_employe_tut']).strip(), id_etp=Get.get_entreprise_by_nom(str(row['service_adm_nom_service']).strip()).id_etp, civilite=str(row['civilite_employe_tut']).strip(), tel=str(row['tel_employe_tut']).strip(), gsm=str(row['gsm_employe_tut']).strip(), mail=str(row['mail_employe_tut']).strip(), id_tut_pro=Get.get_tuteur_pro_last_id() + 1)
            
            if str(row['dtdeb_stage']).strip() != '' and str(row['dtfin_stage']).strip() != '':
                dt_deb_split = str(row['dtdeb_stage']).strip().split('/')
                dt_fin_split = str(row['dtfin_stage']).strip().split('/')
                dt_debut = date.fromisoformat(f'{dt_deb_split[2]}-{dt_deb_split[1]}-{dt_deb_split[0]}')
                dt_fin = date.fromisoformat(f'{dt_fin_split[2]}-{dt_fin_split[1]}-{dt_fin_split[0]}')
            else:
                dt_debut = None
                dt_fin = None
            
            if str(row['duree']).strip() != '':
                duree = int(str(row['duree']).strip().split('.')[0])
            else:
                duree = None
            
            Insert.insert_stage_alt(Get.get_entreprise_by_nom(str(row['service_adm_nom_service']).strip()).id_etp, Get.get_tuteur_pro_by_nom_prenom(str(row['nom_employe_tut']).strip(), str(row['prenom_employe_tut']).strip()).id_tut_pro, None, Get.get_etudiant_by_nom_prenom(str(row['nom_stagiaire']).strip(), str(row['prenom_stagaire']).strip()).id_etu, titre=str(row['titre_stage']).strip(), theme=str(row['theme_stage']).strip(), intitule_env=str(row['intitule_env_stage']).strip(), dt_debut=dt_debut, dt_fin=dt_fin, duree=duree, id_stg_alt=Get.get_stg_alt_last_id() + 1)
    
    @staticmethod
    def stagiaires_from_excel(excel_path: str) -> None:
        # Lire le fichier Excel
        stagiaires_df = pd.read_excel(excel_path)
        
        # Remplacer les nan par des chaînes vides
        stagiaires_df.fillna('', inplace=True)
        
        # Mettre le type de la colonne 'duree' en str
        stagiaires_df['duree'] = stagiaires_df['duree'].astype(str)
        
        for _, row in stagiaires_df.iterrows():
            if Get.get_etudiant_by_nom_prenom(str(row['nom_stagiaire']).strip(), str(row['prenom_stagaire']).strip()) is None:
                Insert.insert_etudiant(str(row['nom_stagiaire']).strip(), str(row['prenom_stagaire']).strip(), False, num=str(row['ine']).strip(),civilite=str(row['civilite_stagiaire']).strip(), id_etu=Get.get_etudiant_last_id() + 1)
                
            if Get.get_entreprise_by_nom(str(row['service_adm_nom_service']).strip()) is None:
                Insert.insert_entreprise(str(row['service_adm_nom_service']).strip(), str(row['service_adm_ville_service']).strip(), str(row['service_adm_cp_service']).strip(), id_etp=Get.get_entreprise_last_id() + 1)
                
            if Get.get_tuteur_pro_by_nom_prenom(str(row['nom_employe_tut']).strip(), str(row['prenom_employe_tut']).strip()) is None:
                Insert.insert_tuteur_pro(str(row['nom_employe_tut']).strip(), str(row['prenom_employe_tut']).strip(), id_etp=Get.get_entreprise_by_nom(str(row['service_adm_nom_service']).strip()).id_etp, civilite=str(row['civilite_employe_tut']).strip(), tel=str(row['tel_employe_tut']).strip(), gsm=str(row['gsm_employe_tut']).strip(), mail=str(row['mail_employe_tut']).strip(), id_tut_pro=Get.get_tuteur_pro_last_id() + 1)
            
            if str(row['dtdeb_stage']).strip() != '' and str(row['dtfin_stage']).strip() != '' and str(row['dtdeb_stage']).strip() != 'NaT' and str(row['dtfin_stage']).strip() != 'NaT':
                dt_debut = date.fromisoformat(str(row['dtdeb_stage']).strip().split(' ')[0])
                dt_fin = date.fromisoformat(str(row['dtfin_stage']).strip().split(' ')[0])
            else:
                dt_debut = None
                dt_fin = None
            
            if str(row['duree']).strip() != '':
                duree = int(str(row['duree']).strip().split('.')[0])
            else:
                duree = None
            
            Insert.insert_stage_alt(Get.get_entreprise_by_nom(str(row['service_adm_nom_service']).strip()).id_etp, Get.get_tuteur_pro_by_nom_prenom(str(row['nom_employe_tut']).strip(), str(row['prenom_employe_tut']).strip()).id_tut_pro, None, Get.get_etudiant_by_nom_prenom(str(row['nom_stagiaire']).strip(), str(row['prenom_stagaire']).strip()).id_etu, titre=str(row['titre_stage']).strip(), theme=str(row['theme_stage']).strip(), intitule_env=str(row['intitule_env_stage']).strip(), dt_debut=dt_debut, dt_fin=dt_fin, duree=duree, id_stg_alt=Get.get_stg_alt_last_id() + 1)


# ExternalDataInserter.alternants_from_csv('D:/Dev/SAE_Stage_Alternance/SAE_Soutenance_App_Stage/data_test/alternant/Alternant - BUT3 Sujet.csv')
# ExternalDataInserter.stagiaires_from_csv('D:/Dev/SAE_Stage_Alternance/SAE_Soutenance_App_Stage/data_test/stagiaire/tableur stages 2023 2024 extraction AREXIS.xls - Extraction.csv')