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

from django.db.models.manager import BaseManager

class GetAll:
    @staticmethod
    def get_all_date_horaire() -> list:
        return DateHoraire.objects.all()

    @staticmethod
    def get_all_entreprise() -> list:
        return Entreprise.objects.all()
    
    @staticmethod
    def get_all_est_dans_promotion() -> list:
        return EstDansPromotion.objects.prefetch_related('etudiant', 'promotion').all()
    
    @staticmethod
    def get_all_est_responsable() -> list:
        return EstResponsable.objects.prefetch_related('professeur', 'promotion').all()
    
    @staticmethod
    def get_all_etudiant() -> list:
        return Etudiant.objects.all()
    
    @staticmethod
    def get_all_inscription_soutenance() -> list:
        return InscriptionSoutenance.objects.prefetch_related('soutenance', 'prof').all()
    
    @staticmethod
    def get_all_inscription_suivi() -> list:
        return InscriptionSuivi.objects.prefetch_related('stg_alt', 'prof').all()
    
    @staticmethod
    def get_all_professeur() -> list:
        return Professeur.objects.all()
    
    @staticmethod
    def get_all_promotion() -> list:
        return Promotion.objects.all()
    
    @staticmethod
    def get_all_salle() -> list:
        return Salle.objects.all()
    
    @staticmethod
    def get_all_secretaire() -> list:
        return Secretaire.objects.all()
    
    @staticmethod
    def get_all_soutenance() -> list:
        return Soutenance.objects.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').all()
    
    @staticmethod
    def get_all_stage_alt() -> list:
        return StageAlt.objects.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').all()
    
    @staticmethod
    def get_all_tuteur_pro() -> list:
        return TuteurPro.objects.prefetch_related('entreprise').all()

class GetById:
    @staticmethod
    def get_date_horaire_by_id(id: int) -> DateHoraire:
        return DateHoraire.objects.get(id_date_horaire=id)

    @staticmethod
    def get_entreprise_by_id(id: int) -> Entreprise:
        return Entreprise.objects.get(id_etp=id)
    
    @staticmethod
    def get_est_dans_promotion_by_etu_id(id: int) -> BaseManager[EstDansPromotion]:
        return EstDansPromotion.objects.prefetch_related('etudiant', 'promotion').filter(etudiant=GetById.get_etudiant_by_id(id)).all()
    
    @staticmethod
    def get_est_dans_promotion(id_etu: int, id_promo: int) -> EstDansPromotion:
        return EstDansPromotion.objects.prefetch_related('etudiant', 'promotion').filter(etudiant=GetById.get_etudiant_by_id(id_etu), promotion=GetById.get_promotion_by_id(id_promo)).first()
    
    @staticmethod
    def get_est_responsable_by_prof_id(id: int) -> list:
        return EstResponsable.objects.prefetch_related('professeur', 'promotion').filter(professeur=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_etudiant_by_id(id: int) -> Etudiant:
        return Etudiant.objects.get(id_etu=id)
    
    @staticmethod
    def get_inscription_soutenance_by_soutenance_id(id: int) -> list:
        return InscriptionSoutenance.objects.prefetch_related('soutenance', 'prof').filter(soutenance=GetById.get_soutenance_by_id(id)).all()
    
    @staticmethod
    def get_inscription_soutenance_by_prof_id(id: int) -> list:
        return InscriptionSoutenance.objects.prefetch_related('soutenance', 'prof').filter(prof=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_inscription_suivi_by_stg_id(id: int) -> list:
        return InscriptionSuivi.objects.prefetch_related('stg_alt', 'prof').filter(stg_alt=GetById.get_stage_alt_by_id(id)).all()
    
    @staticmethod
    def get_inscription_suivi_by_prof_id(id: int) -> list:
        return InscriptionSuivi.objects.prefetch_related('stg_alt', 'prof').filter(prof=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_professeur_by_id(id: int) -> Professeur:
        return Professeur.objects.get(id_prof=id)
    
    @staticmethod
    def get_promotion_by_id(id: int) -> Promotion:
        return Promotion.objects.get(id_promo=id)
    
    @staticmethod
    def get_salle_by_id(id: int) -> Salle:
        return Salle.objects.get(id_salle=id)
    
    @staticmethod
    def get_secretaire_by_id(id: int) -> Secretaire:
        return Secretaire.objects.get(id_sec=id)
    
    @staticmethod
    def get_soutenance_by_id(id: int) -> Soutenance:
        return Soutenance.objects.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').get(id_sout=id)
    
    @staticmethod
    def get_stage_alt_by_id(id: int) -> StageAlt:
        return StageAlt.objects.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').get(id_stg_alt=id)
    
    @staticmethod
    def get_tuteur_pro_by_id(id: int) -> TuteurPro:
        return TuteurPro.objects.prefetch_related('entreprise').get(id_tut_pro=id)
    
class Get:
    @staticmethod
    def get_etudiants_by_tuteur_pro_id(id: int) -> list:
        return Etudiant.objects.prefetch_related('tuteur_pro').filter(tuteur_pro=GetById.get_tuteur_pro_by_id(id)).all()
    
    @staticmethod
    def get_soutenance_by_etu_id(id: int) -> list:
        return Soutenance.objects.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').filter(stg_alt=GetById.get_stage_alt_by_id(id)).all()
    
    @staticmethod
    def get_soutenance_by_prof_candide_id(id: int) -> list:
        return Soutenance.objects.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').filter(prof_candide=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_soutenance_by_stg_alt_id(id: int) -> list:
        return Soutenance.objects.prefetch_related('stg_alt', 'horaire', 'salle', 'prof_candide').filter(stg_alt=GetById.get_stage_alt_by_id(id)).all()
    
    @staticmethod
    def get_stage_alt_by_etu_id(id: int) -> BaseManager[StageAlt]:
        return StageAlt.objects.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').filter(etudiant=GetById.get_etudiant_by_id(id)).all()
    
    @staticmethod
    def get_stage_alt_by_tuteur_pro_id(id: int) -> list:
        return StageAlt.objects.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').filter(tuteur_pro=GetById.get_tuteur_pro_by_id(id)).all()
    
    @staticmethod
    def get_stage_alt_by_tuteur_univ_id(id: int) -> list:
        return StageAlt.objects.prefetch_related('entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant').filter(tuteur_univ=GetById.get_professeur_by_id(id)).all()
    
    @staticmethod
    def get_etudiant_by_nom_prenom(nom: str, prenom: str) -> Etudiant:
        return Etudiant.objects.filter(nom_etu=nom, prenom_etu=prenom).first()
    
    @staticmethod
    def get_etudiant_last_id() -> int:
        return Etudiant.objects.last().id_etu if Etudiant.objects.last() else 0
    
    @staticmethod
    def get_promotion_by_annee_filiere(annee: int, filiere: str) -> Promotion:
        return Promotion.objects.filter(annee_promo=annee, filiere_promo=filiere).first()
    
    @staticmethod
    def get_promotion_last_id() -> int:
        return Promotion.objects.last().id_promo if Promotion.objects.last() else 0
    
    @staticmethod
    def get_professeur_by_nom_prenom(nom: str, prenom: str) -> Professeur:
        return Professeur.objects.filter(nom_prof=nom, prenom_prof=prenom).first()
    
    @staticmethod
    def get_professeur_last_id() -> int:
        return Professeur.objects.last().id_prof if Professeur.objects.last() else 0
    
    @staticmethod
    def get_entreprise_by_nom(nom: str) -> Entreprise:
        return Entreprise.objects.filter(nom_etp=nom).first()
    
    @staticmethod
    def get_entreprise_last_id() -> int:
        return Entreprise.objects.last().id_etp if Entreprise.objects.last() else 0
    
    @staticmethod
    def get_tuteur_pro_by_nom(nom: str) -> TuteurPro:
        return TuteurPro.objects.filter(nom_tut_pro=nom).first()
    
    @staticmethod
    def get_tuteur_pro_by_nom_prenom(nom: str, prenom: str) -> TuteurPro:
        return TuteurPro.objects.filter(nom_tut_pro=nom, prenom_tut_pro=prenom).first()
    
    @staticmethod
    def get_tuteur_pro_last_id() -> int:
        return TuteurPro.objects.last().id_tut_pro if TuteurPro.objects.last() else 0
    
    @staticmethod
    def get_stg_alt_last_id() -> int:
        return StageAlt.objects.last().id_stg_alt if StageAlt.objects.last() else 0
    
    @staticmethod
    def get_etudiant_by_tuteur_pro_id(id: int) -> list:
        stg_alt = StageAlt.objects.filter(tuteur_pro=GetById.get_tuteur_pro_by_id(id)).all()
        print(stg_alt.count())
        list_etu = []
        for stg in stg_alt:
            list_etu.append(stg.etudiant)
        return list_etu
    
    @staticmethod
    def get_soutenance_by_tuteur_pro_id(id: int) -> list:
        list_soutenance = []
        for soutenance in GetAll.get_all_soutenance():
            if( soutenance.stg_alt.tuteur_pro.id_tut_pro == id):
                list_soutenance.append(soutenance)
        return list_soutenance
    
    @staticmethod 
    def get_secretaire_by_nom_prenom(nom: str, prenom: str) -> Secretaire:
        return Secretaire.objects.filter(nom_sec=nom, prenom_sec=prenom).first()
    
    @staticmethod
    def get_etudiant_by_id_connection(id_connection: str) -> Etudiant:
        return Etudiant.objects.filter(id_connection=id_connection).first()
    
    @staticmethod
    def get_professeur_by_id_connection(id_connection: str) -> Professeur:
        return Professeur.objects.filter(id_connection=id_connection).first()
    
    @staticmethod
    def get_secretaire_by_id_connection(id_connection: str) -> Secretaire:
        return Secretaire.objects.filter(id_connection=id_connection).first()
    
    @staticmethod
    def get_tuteur_pro_by_id_connection(id_connection: str) -> TuteurPro:
        return TuteurPro.objects.filter(id_connection=id_connection).first()

    @staticmethod
    def get_all_soutenance_prof(id_prof: int) -> list:
        list_sout = []
        for sout in GetAll.get_all_soutenance():
            if sout.prof_candide is not None and sout.prof_candide.id_prof == id_prof:
                list_sout.append(sout)
            elif sout.stg_alt.tuteur_univ.id_prof == id_prof:
                list_sout.append(sout)
        return list_sout

    @staticmethod
    def get_all_soutenance_without_candide(id_prof: int) -> list:
        list_sout = []
        for sout in GetAll.get_all_soutenance():
            if sout.prof_candide is None and sout.stg_alt.tuteur_univ.id_prof != id_prof:
                list_sout.append(sout)
        return list_sout
    
    @staticmethod
    def get_all_studients_by_tuteur_univ(id_prof: int) -> list:
        list_stg = []
        for stg in GetAll.get_all_stage_alt():
            if stg.tuteur_univ is not None and stg.tuteur_univ.id_prof == id_prof:
                list_stg.append(stg.etudiant)
        return list_stg
    
    @staticmethod
    def get_all_candide_by_soutenance(id_sout: int) -> list:
        list_cand = []
        for ins in GetAll.get_all_inscription_soutenance():
            if ins.soutenance is not None and ins.soutnance.id == id_sout:
                list_cand.append(ins.prof)
        return list_cand
    
    @staticmethod
    def get_horaire_by_date_heure(date: str, heure: str) -> DateHoraire:
        return DateHoraire.objects.filter(dt_date=date, heure=heure).first()
    
    @staticmethod
    def get_last_id_date_horaire() -> int:
        return DateHoraire.objects.last().id_date_horaire if DateHoraire.objects.last() else 0
    
    @staticmethod
    def get_last_id_soutenance() -> int:
        return Soutenance.objects.last().id_sout if Soutenance.objects.last() else 0
    
    @staticmethod
    def get_stg_alt_by_titre_theme_intitule_dt_debut_dt_fin_duree_entreprise_tuteur_pro_tuteur_univ_etudiant(titre: str, theme: str, intitule: str, dt_debut: str, dt_fin: str, duree: int, entreprise: Entreprise, tuteur_pro: TuteurPro, tuteur_univ: Professeur, etudiant: Etudiant) -> StageAlt:
        return StageAlt.objects.filter(titre_stg_alt=titre, theme_stg_alt=theme, intitule_env_stg_alt=intitule, dt_date_debut_stg_alt=dt_debut, dt_date_fin_stg_alt=dt_fin, duree_stg_alt=duree, entreprise=entreprise, tuteur_pro=tuteur_pro, tuteur_univ=tuteur_univ, etudiant=etudiant).first()
    
    @staticmethod
    def get_soutenance_by_salle_id(id: int) -> list:
        return Soutenance.objects.filter(salle=GetById.get_salle_by_id(id)).all()
    
    @staticmethod
    def get_salle_est_libre(id_salle: int, id_date_horaire) -> bool:
        for soutenance in Get.get_soutenance_by_salle_id(id_salle):
            if soutenance.horaire.id_date_horaire == id_date_horaire:
                return False
        return True
    
    @staticmethod
    def get_soutenance_by_etudiant_id(id: int) -> list:
        list_soutenance = []
        for soutenance in GetAll.get_all_soutenance():
            if soutenance.stg_alt.etudiant.id_etu == id:
                list_soutenance.append(soutenance)
        return list_soutenance
    
    @staticmethod
    def get_stage_wout_tuteur_pro() -> list:
        list_stage = []
        for stage in GetAll.get_all_stage_alt():
            if stage.tuteur_univ is None:
                list_stage.append(stage)
        return list_stage
    
    @staticmethod
    def get_inscritpion_suivi_by_prof_id_stage_id(id_prof: int, id_stage: int) -> InscriptionSuivi:
        return InscriptionSuivi.objects.filter(prof=GetById.get_professeur_by_id(id_prof), stg_alt=GetById.get_stage_alt_by_id(id_stage)).first()
