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
    def get_all_date_horaire() -> list:
        return DateHoraire.query.all()

    @staticmethod
    def get_all_entreprise() -> list:
        return Entreprise.query.all()
    
    @staticmethod
    def get_all_est_dans_promotion() -> list:
        return EstDansPromotion.prefetch_related('etudiant', 'promotion').all()
    
    @staticmethod
    def get_all_est_responsable() -> list:
        return EstResponsable.prefetch_related('professeur', 'promotion').all()
    
    @staticmethod
    def get_all_etudiant() -> list:
        return Etudiant.query.all()
    
    @staticmethod
    def get_all_inscription_soutenance() -> list:
        return InscriptionSoutenance.prefetch_related('soutenance', 'prof').all()
    
    @staticmethod
    def get_all_inscription_suivi() -> list:
        return InscriptionSuivi.prefetch_related('stg_alt', 'prof').all()
    
    @staticmethod
    def get_all_professeur() -> list:
        return Professeur.query.all()
    
    @staticmethod
    def get_all_promotion() -> list:
        return Promotion.query.all()
    
    @staticmethod
    def get_all_salle() -> list:
        return Salle.query.all()
    
    @staticmethod
    def get_all_secretaire() -> list:
        return Secretaire.query.all()
    
    @staticmethod
    def get_all_soutenance() -> list:
        return Soutenance.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').all()
    
    @staticmethod
    def get_all_stage_alt() -> list:
        return StageAlt.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').all()
    
    @staticmethod
    def get_all_tuteur_pro() -> list:
        return TuteurPro.prefetch_related('entreprise').all()

class GetById:
    @staticmethod
    def get_date_horaire_by_id(id: int) -> DateHoraire:
        return DateHoraire.query.get(id)

    @staticmethod
    def get_entreprise_by_id(id: int) -> Entreprise:
        return Entreprise.query.get(id)
    
    @staticmethod
    def get_est_dans_promotion_by_etu_id(id: int) -> list:
        return EstDansPromotion.prefetch_related('etudiant', 'promotion').filter(etudiant=GetById.get_etudiant_by_id(id)).all()
    
    @staticmethod
    def get_est_responsable_by_prof_id(id: int) -> list:
        return EstResponsable.prefetch_related('professeur', 'promotion').filter(professeur=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_etudiant_by_id(id: int) -> Etudiant:
        return Etudiant.query.get(id)
    
    @staticmethod
    def get_inscription_soutenance_by_soutenance_id(id: int) -> list:
        return InscriptionSoutenance.prefetch_related('soutenance', 'prof').filter(soutenance=GetById.get_soutenance_by_id(id)).all()
    
    @staticmethod
    def get_inscription_soutenance_by_prof_id(id: int) -> list:
        return InscriptionSoutenance.prefetch_related('soutenance', 'prof').filter(prof=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_inscription_suivi_by_stg_id(id: int) -> list:
        return InscriptionSuivi.prefetch_related('stg_alt', 'prof').filter(stg_alt=GetById.get_stage_alt_by_id(id)).all()
    
    @staticmethod
    def get_inscription_suivi_by_prof_id(id: int) -> list:
        return InscriptionSuivi.prefetch_related('stg_alt', 'prof').filter(prof=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_professeur_by_id(id: int) -> Professeur:
        return Professeur.query.get(id)
    
    @staticmethod
    def get_promotion_by_id(id: int) -> Promotion:
        return Promotion.query.get(id)
    
    @staticmethod
    def get_salle_by_id(id: int) -> Salle:
        return Salle.query.get(id)
    
    @staticmethod
    def get_secretaire_by_id(id: int) -> Secretaire:
        return Secretaire.query.get(id)
    
    @staticmethod
    def get_soutenance_by_id(id: int) -> Soutenance:
        return Soutenance.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').get(id)
    
    @staticmethod
    def get_stage_alt_by_id(id: int) -> StageAlt:
        return StageAlt.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').get(id)
    
    @staticmethod
    def get_tuteur_pro_by_id(id: int) -> TuteurPro:
        return TuteurPro.prefetch_related('entreprise').get(id)
    
class Get:
    @staticmethod
    def get_etudiants_by_tuteur_pro_id(id: int) -> list:
        return Etudiant.prefetch_related('tuteur_pro').filter(tuteur_pro=GetById.get_tuteur_pro_by_id(id)).all()