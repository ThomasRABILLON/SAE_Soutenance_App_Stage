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

class Update:
    @staticmethod
    def update_date_horaire(date_horaire: DateHoraire) -> bool:
        try:
            date_horaire.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_entreprise(entreprise: Entreprise) -> bool:
        try:
            entreprise.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_est_dans_promotion(est_dans_promotion: EstDansPromotion) -> bool:
        try:
            est_dans_promotion.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_est_responsable(est_responsable: EstResponsable) -> bool:
        try:
            est_responsable.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_etudiant(etudiant: Etudiant) -> bool:
        try:
            etudiant.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_inscription_soutenance(inscription_soutenance: InscriptionSoutenance) -> bool:
        try:
            inscription_soutenance.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_inscription_suivi(inscription_suivi: InscriptionSuivi) -> bool:
        try:
            inscription_suivi.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_professeur(professeur: Professeur) -> bool:
        try:
            professeur.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_promotion(promotion: Promotion) -> bool:
        try:
            promotion.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_salle(salle: Salle) -> bool:
        try:
            salle.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_secretaire(secretaire: Secretaire) -> bool:
        try:
            secretaire.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_soutenance(soutenance: Soutenance) -> bool:
        try:
            soutenance.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_stage_alt(stage_alt: StageAlt) -> bool:
        try:
            stage_alt.save()
            return True
        except:
            return False
    
    @staticmethod
    def update_tuteur_pro(tuteur_pro: TuteurPro) -> bool:
        try:
            tuteur_pro.save()
            return True
        except:
            return False