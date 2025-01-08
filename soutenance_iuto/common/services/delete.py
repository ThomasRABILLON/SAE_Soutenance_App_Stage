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
    def delete_date_horaire(self, date_horaire: DateHoraire) -> bool:
        try:
            date_horaire.delete()
            return True
        except:
            return False
    
    def delete_entreprise(self, entreprise: Entreprise) -> bool:
        try:
            entreprise.delete()
            return True
        except:
            return False
    
    def delete_est_dans_promotion(self, est_dans_promotion: EstDansPromotion) -> bool:
        try:
            est_dans_promotion.delete()
            return True
        except:
            return False
    
    def delete_est_responsable(self, est_responsable: EstResponsable) -> bool:
        try:
            est_responsable.delete()
            return True
        except:
            return False
    
    def delete_etudiant(self, etudiant: Etudiant) -> bool:
        try:
            etudiant.delete()
            return True
        except:
            return False
    
    def delete_inscription_soutenance(self, inscription_soutenance: InscriptionSoutenance) -> bool:
        try:
            inscription_soutenance.delete()
            return True
        except:
            return False
    
    def delete_inscription_suivi(self, inscription_suivi: InscriptionSuivi) -> bool:
        try:
            inscription_suivi.delete()
            return True
        except:
            return False
    
    def delete_professeur(self, professeur: Professeur) -> bool:
        try:
            professeur.delete()
            return True
        except:
            return False

    def delete_promotion(self, promotion: Promotion) -> bool:
        try:
            promotion.delete()
            return True
        except:
            return False
    
    def delete_salle(self, salle: Salle) -> bool:
        try:
            salle.delete()
            return True
        except:
            return False
    
    def delete_secretaire(self, secretaire: Secretaire) -> bool:
        try:
            secretaire.delete()
            return True
        except:
            return False
    
    def delete_soutenance(self, soutenance: Soutenance) -> bool:
        try:
            soutenance.delete()
            return True
        except:
            return False
    
    def delete_stage_alt(self, stage_alt: StageAlt) -> bool:
        try:
            stage_alt.delete()
            return True
        except:
            return False
    
    def delete_tuteur_pro(self, tuteur_pro: TuteurPro) -> bool:
        try:
            tuteur_pro.delete()
            return True
        except:
            return False
    
    