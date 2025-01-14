from common.models.DateHoraire import DateHoraire
from common.models.Entreprise import Entreprise
from common.models.EstDansPromotion import EstDansPromotion
from common.models.EstResponsable import EstResponsable
from common.models.Etudiant import Etudiant
from common.models.InscriptionSoutenance import InscriptionSoutenance
from common.models.InscriptionSuivi import InscriptionSuivi
from common.models.Professeur import Professeur
from common.models.Promotion import Promotion
from common.models.Salle import Salle
from common.models.Secretaire import Secretaire
from common.models.Soutenance import Soutenance
from common.models.StageAlt import StageAlt
from common.models.TuteurPro import TuteurPro

class Delete:
    @staticmethod
    def delete_date_horaire(date_horaire: DateHoraire) -> bool:
        try:
            date_horaire.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_entreprise(entreprise: Entreprise) -> bool:
        try:
            entreprise.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_est_dans_promotion(est_dans_promotion: EstDansPromotion) -> bool:
        try:
            est_dans_promotion.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_est_responsable(est_responsable: EstResponsable) -> bool:
        try:
            est_responsable.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_etudiant(etudiant: Etudiant) -> bool:
        try:
            etudiant.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_inscription_soutenance(inscription_soutenance: InscriptionSoutenance) -> bool:
        try:
            inscription_soutenance.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_inscription_suivi(inscription_suivi: InscriptionSuivi) -> bool:
        try:
            inscription_suivi.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_professeur(professeur: Professeur) -> bool:
        try:
            professeur.delete()
            return True
        except:
            return False

    @staticmethod
    def delete_promotion(promotion: Promotion) -> bool:
        try:
            promotion.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_salle(salle: Salle) -> bool:
        try:
            salle.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_secretaire(secretaire: Secretaire) -> bool:
        try:
            secretaire.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_soutenance(soutenance: Soutenance) -> bool:
        try:
            soutenance.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_stage_alt(stage_alt: StageAlt) -> bool:
        try:
            stage_alt.delete()
            return True
        except:
            return False
    
    @staticmethod
    def delete_tuteur_pro(tuteur_pro: TuteurPro) -> bool:
        try:
            tuteur_pro.delete()
            return True
        except:
            return False
    
    