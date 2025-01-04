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

from datetime import date, time

class Insert:
    def insert_date_horaire(self, dt_date: date, heure: time, duree: int, id_date_horaire: int = -1) -> bool:
        try:
            if duree < 0:
                return False
            
            if id_date_horaire == -1:
                DateHoraire.objects.create(
                    dt_date=dt_date,
                    heure=heure,
                    duree=duree
                ).save()
            else:            
                DateHoraire.objects.create(
                    id_date_horaire=id_date_horaire,
                    dt_date=dt_date,
                    heure=heure,
                    duree=duree
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_entreprise(self, nom_etp: str, cp_etp: str, ville_etp: str, id_etp: int = -1) -> bool:
        try:
            if id_etp == -1:
                Entreprise.objects.create(
                    nom_etp=nom_etp,
                    cp_etp=cp_etp,
                    ville_etp=ville_etp
                ).save()
            else:
                Entreprise.objects.create(
                    id_etp=id_etp,
                    nom_etp=nom_etp,
                    cp_etp=cp_etp,
                    ville_etp=ville_etp
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_est_dans_promotion(self, id_etu: int, id_promo: int) -> bool:
        try:
            EstDansPromotion.objects.create(
                etudiant=Etudiant.objects.get(id_etu=id_etu),
                promotion=Promotion.objects.get(id_promo=id_promo)
            ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_est_responsable(self, id_prof: int, id_promo: int) -> bool:
        try:
            EstResponsable.objects.create(
                professeur=Professeur.objects.get(id_prof=id_prof),
                promotion=Promotion.objects.get(id_promo=id_promo)
            ).save()
            return True
        except Exception as e:
            # print(e)
            return False
        
    def insert_etudiant(self, num: str, ine: str, civilite: str, nom: str, prenom: str, mail: str, alternant: bool, id_etu: int = -1) -> bool:
        try:
            if id_etu == -1:
                Etudiant.objects.create(
                    num_etu=num,
                    ine_etu=ine,
                    civilite_etu=civilite,
                    nom_etu=nom,
                    prenom_etu=prenom,
                    mail_etu=mail,
                    alternant=alternant
                ).save()
            else:
                Etudiant.objects.create(
                    id_etu=id_etu,
                    num_etu=num,
                    ine_etu=ine,
                    civilite_etu=civilite,
                    nom_etu=nom,
                    prenom_etu=prenom,
                    mail_etu=mail,
                    alternant=alternant
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_inscription_soutenance(self, id_sout: int, id_prof: int) -> bool:
        try:
            InscriptionSoutenance.objects.create(
                soutenance=Soutenance.objects.get(id_sout=id_sout),
                prof=Professeur.objects.get(id_prof=id_prof)
            ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_inscription_suivi(self, id_stg_alt: int, id_prof: int) -> bool:
        try:
            InscriptionSuivi.objects.create(
                stg_alt=StageAlt.objects.get(id_stg_alt=id_stg_alt),
                prof=Professeur.objects.get(id_prof=id_prof)
            ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_professeur(self, num: str, civilite: str, nom: str, prenom: str, mail: str, id_prof: int = -1) -> bool:
        try:
            if id_prof == -1:
                Professeur.objects.create(
                    num_prof=num,
                    civilite_prof=civilite,
                    nom_prof=nom,
                    prenom_prof=prenom,
                    mail_prof=mail
                ).save()
            else:
                Professeur.objects.create(
                    id_prof=id_prof,
                    num_prof=num,
                    civilite_prof=civilite,
                    nom_prof=nom,
                    prenom_prof=prenom,
                    mail_prof=mail
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_promotion(self, annee: int, filiere: str, id_promo: int = -1) -> bool:
        try:
            if id_promo == -1:
                Promotion.objects.create(
                    annee_promo=annee,
                    filiere_promo=filiere
                ).save()
            else:
                Promotion.objects.create(
                    id_promo=id_promo,
                    annee_promo=annee,
                    filiere_promo=filiere
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_salle(self, nom: str, id_salle: int = -1) -> bool:
        try:
            if id_salle == -1:
                Salle.objects.create(
                    nom_salle=nom
                ).save()
            else:
                Salle.objects.create(
                    id_salle=id_salle,
                    nom_salle=nom
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_secretaire(self, nom: str, prenom: str, mail: str, id_sec: int = -1) -> bool:
        try:
            if id_sec == -1:
                Secretaire.objects.create(
                    nom_sec=nom,
                    prenom_sec=prenom,
                    mail_sec=mail
                ).save()
            else:
                Secretaire.objects.create(
                    id_sec=id_sec,
                    nom_sec=nom,
                    prenom_sec=prenom,
                    mail_sec=mail
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_soutenance(self, id_stg_alt: int, id_date_horaire: int, id_salle: int, id_prof: int, id_soutenance: int = -1) -> bool:
        try:
            if id_soutenance == -1:
                Soutenance.objects.create(
                    stg_alt=StageAlt.objects.get(id_stg_alt=id_stg_alt),
                    horaire=DateHoraire.objects.get(id_date_horaire=id_date_horaire),
                    salle=Salle.objects.get(id_salle=id_salle),
                    prof_candide=Professeur.objects.get(id_prof=id_prof)
                ).save()
            else:
                Soutenance.objects.create(
                    id_sout=id_soutenance,
                    stg_alt=StageAlt.objects.get(id_stg_alt=id_stg_alt),
                    horaire=DateHoraire.objects.get(id_date_horaire=id_date_horaire),
                    salle=Salle.objects.get(id_salle=id_salle),
                    prof_candide=Professeur.objects.get(id_prof=id_prof)
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_stage_alt(self, titre: str, theme: str, intitule_env: str, dt_debut: date, dt_fin: date, duree: int, id_etp: int, id_tuteur_pro: int, id_tuteur_univ: int, id_etu: int, id_stg_alt: int = -1) -> bool:
        try:
            if id_stg_alt == -1:
                StageAlt.objects.create(
                    titre_stg_alt=titre,
                    theme_stg_alt=theme,
                    intitule_env_stg_alt=intitule_env,
                    dt_date_debut_stg_alt=dt_debut,
                    dt_date_fin_stg_alt=dt_fin,
                    duree_stg_alt=duree,
                    entreprise=Entreprise.objects.get(id_etp=id_etp),
                    tuteur_pro=TuteurPro.objects.get(id_tut_pro=id_tuteur_pro),
                    tuteur_univ=Professeur.objects.get(id_prof=id_tuteur_univ),
                    etudiant=Etudiant.objects.get(id_etu=id_etu)
                ).save()
            else:
                StageAlt.objects.create(
                    id_stg_alt=id_stg_alt,
                    titre_stg_alt=titre,
                    theme_stg_alt=theme,
                    intitule_env_stg_alt=intitule_env,
                    dt_date_debut_stg_alt=dt_debut,
                    dt_date_fin_stg_alt=dt_fin,
                    duree_stg_alt=duree,
                    entreprise=Entreprise.objects.get(id_etp=id_etp),
                    tuteur_pro=TuteurPro.objects.get(id_tut_pro=id_tuteur_pro),
                    tuteur_univ=Professeur.objects.get(id_prof=id_tuteur_univ),
                    etudiant=Etudiant.objects.get(id_etu=id_etu)
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False
    
    def insert_tuteur_pro(self, civilite: str, nom: str, prenom: str, tel: str, gsm: str, mail: str, id_etp: int, id_tut_pro: int = -1) -> bool:
        try:
            if id_tut_pro == -1:
                TuteurPro.objects.create(
                    civilite_tut_pro=civilite,
                    nom_tut_pro=nom,
                    prenom_tut_pro=prenom,
                    tel_tut_pro=tel,
                    gsm_tut_pro=gsm,
                    mail_tut_pro=mail,
                    entreprise=Entreprise.objects.get(id_etp=id_etp)
                ).save()
            else:
                TuteurPro.objects.create(
                    id_tut_pro=id_tut_pro,
                    civilite_tut_pro=civilite,
                    nom_tut_pro=nom,
                    prenom_tut_pro=prenom,
                    tel_tut_pro=tel,
                    gsm_tut_pro=gsm,
                    mail_tut_pro=mail,
                    entreprise=Entreprise.objects.get(id_etp=id_etp)
                ).save()
            return True
        except Exception as e:
            # print(e)
            return False