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

class GetAll:
    @staticmethod
    def get_all_date_horaire():
        return DateHoraire.query.all()

    @staticmethod
    def get_all_entreprise():
        return Entreprise.query.all()
    
    @staticmethod
    def get_all_est_dans_promotion():
        return EstDansPromotion.query.all()
    
    @staticmethod
    def get_all_est_responsable():
        return EstResponsable.query.all()
    
    @staticmethod
    def get_all_etudiant():
        return Etudiant.query.all()
    
    @staticmethod
    def get_all_inscription_soutenance():
        return InscriptionSoutenance.query.all()
    
    @staticmethod
    def get_all_inscription_suivi():
        return InscriptionSuivi.query.all()
    
    @staticmethod
    def get_all_professeur():
        return Professeur.query.all()
    
    @staticmethod
    def get_all_promotion():
        return Promotion.query.all()
    
    @staticmethod
    def get_all_salle():
        return Salle.query.all()
    
    @staticmethod
    def get_all_secretaire():
        return Secretaire.query.all()
    
    @staticmethod
    def get_all_soutenance():
        return Soutenance.query.all()
    
    @staticmethod
    def get_all_stage_alt():
        return StageAlt.query.all()
    
    @staticmethod
    def get_all_tuteur_pro():
        return TuteurPro.query.all()

class GetById:
    @staticmethod
    def get_date_horaire_by_id(id: int):
        return DateHoraire.query.get(id)

    @staticmethod
    def get_entreprise_by_id(id: int):
        return Entreprise.query.get(id)
    
    @staticmethod
    def get_est_dans_promotion_by_id(id: int):
        return EstDansPromotion.query.get(id)
    
    @staticmethod
    def get_est_responsable_by_id(id: int):
        return EstResponsable.query.get(id)
    
    @staticmethod
    def get_etudiant_by_id(id: int):
        return Etudiant.query.get(id)
    
    @staticmethod
    def get_inscription_soutenance_by_id(id: int):
        return InscriptionSoutenance.query.get(id)
    
    @staticmethod
    def get_inscription_suivi_by_id(id: int):
        return InscriptionSuivi.query.get(id)
    
    @staticmethod
    def get_professeur_by_id(id: int):
        return Professeur.query.get(id)
    
    @staticmethod
    def get_promotion_by_id(id: int):
        return Promotion.query.get(id)
    
    @staticmethod
    def get_salle_by_id(id: int):
        return Salle.query.get(id)
    
    @staticmethod
    def get_secretaire_by_id(id: int):
        return Secretaire.query.get(id)
    
    @staticmethod
    def get_soutenance_by_id(id: int):
        return Soutenance.query.get(id)
    
    @staticmethod
    def get_stage_alt_by_id(id: int):
        return StageAlt.query.get(id)
    
    @staticmethod
    def get_tuteur_pro_by_id(id: int):
        return TuteurPro.query.get(id)