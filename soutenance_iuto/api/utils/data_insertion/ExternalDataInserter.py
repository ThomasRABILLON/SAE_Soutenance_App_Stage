import pandas as pd


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
            # TODO: Insérer les données dans la base de données
            pass
    
    @staticmethod
    def alternants_from_excel(excel_path: str) -> None:
        # Lire le fichier Excel
        alternants_df = pd.read_excel(excel_path)
        
        # Renommer les colonnes nommées 'CP ET VILLE_ENTREPRISE' en 'CP_ENTREPRISE' et 'NOM_MA' en 'CIVILITE_MA'
        alternants_df.rename(columns={'CP ET VILLE_ENTREPRISE': 'CP_ENTREPRISE', 'NOM MA': 'CIVILITE_MA'}, inplace=True)
        # Renommer les colonnes 0, 6 et 8 en 'PROMOTION', 'VILLE_ENTREPRISE' et 'NOM_MA'
        alternants_df.rename(columns={'Unnamed: 0': 'PROMOTION', 'Unnamed: 6': 'VILLE_ENTREPRISE', 'Unnamed: 8': 'NOM_MA'}, inplace=True)
        
        for _, row in alternants_df.iterrows():
            # TODO: Insérer les données dans la base de données
            pass
    
    @staticmethod
    def stagiaires_from_csv(csv_path: str) -> None:
        # Lire le fichier CSV
        stagiaires_df = pd.read_csv(csv_path, sep=',')
        
        for _, row in stagiaires_df.iterrows():
            # TODO: Insérer les données dans la base de données
            pass
    
    @staticmethod
    def stagiaires_from_excel(excel_path: str) -> None:
        # Lire le fichier Excel
        stagiaires_df = pd.read_excel(excel_path)
        
        for _, row in stagiaires_df.iterrows():
            # TODO: Insérer les données dans la base de données
            pass


# ExternalDataInserter.alternants_from_excel('D:/Dev/SAE_Stage_Alternance/SAE_Soutenance_App_Stage/data_test/alternant/Alternant.xlsx')
ExternalDataInserter.stagiaires_from_csv('D:/Dev/SAE_Stage_Alternance/SAE_Soutenance_App_Stage/data_test/stagiaire/tableur stages 2023 2024 extraction AREXIS.xls - Extraction.csv')