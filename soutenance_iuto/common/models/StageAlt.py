import datetime
from common.models import Entreprise, TuteurPro, TuteurUniv, Etudiant


class StageAlt:
    """Classe représentant un stage ou une alternance."""

    def __init__(
        self,
        id_stg_alt: int,
        titre_stg_alt: str,
        theme_stg_alt: str,
        intitule_stg_alt: str,
        dt_date_debut_stg_alt: datetime,
        dt_date_fin_stg_alt: datetime,
        duree_stg_alt: int,
        entreprise: Entreprise,
        tuteur_pro: TuteurPro,
        tuteur_univ: TuteurUniv,
        etudiant: Etudiant,
    ):
        """Constructeur de la classe StageAlt.

        Args:
            id_stg_alt (int): id du stage ou de l'alternance
            titre_stg_alt (str): titre du stage ou de l'alternance
            theme_stg_alt (str): thème du stage ou de l'alternance
            intitule_stg_alt (str): intitulé du stage ou de l'alternance
            dt_date_debut_stg_alt (datetime): date de début du stage ou de l'alternance
            dt_date_fin_stg_alt (datetime): date de fin du stage ou de l'alternance
            duree_stg_alt (int): durée du stage ou de l'alternance
            entreprise (Entreprise): entreprise d'accueil
            tuteur_pro (TuteurPro): tuteur professionnel
            tuteur_univ (TuteurUniv): tuteur universitaire
            etudiant (Etudiant): étudiant
        """
        self._id = id_stg_alt
        self._titre = titre_stg_alt
        self._theme = theme_stg_alt
        self._intitule = intitule_stg_alt
        self._dt_date_debut = dt_date_debut_stg_alt
        self._dt_date_fin = dt_date_fin_stg_alt
        self._duree = duree_stg_alt
        self._entreprise = entreprise
        self._tuteur_pro = tuteur_pro
        self._tuteur_univ = tuteur_univ
        self._etudiant = etudiant

    # Getters

    @property
    def id(self) -> int:
        """Getter de l'attribut _id.

        Returns:
            int: id du stage ou de l'alternance
        """
        return self._id

    @property
    def titre(self) -> str:
        """Getter de l'attribut _titre.

        Returns:
            str: titre du stage ou de l'alternance
        """
        return self._titre

    @property
    def theme(self) -> str:
        """Getter de l'attribut _theme.

        Returns:
            str: thème du stage ou de l'alternance
        """
        return self._theme

    @property
    def intitule(self) -> str:
        """Getter de l'attribut _intitule.

        Returns:
            str: intitulé du stage ou de l'alternance
        """
        return self._intitule

    @property
    def dt_date_debut(self) -> datetime:
        """Getter de l'attribut _dt_date_debut.

        Returns:
            datetime: date de début du stage ou de l'alternance
        """
        return self._dt_date_debut

    @property
    def dt_date_fin(self) -> datetime:
        """Getter de l'attribut _dt_date_fin.

        Returns:
            datetime: date de fin du stage ou de l'alternance
        """
        return self._dt_date_fin

    @property
    def duree_entreprise(self) -> int:
        """Getter de l'attribut _duree.

        Returns:
            int: durée du stage ou de l'alternance
        """
        return self._duree

    @property
    def entreprise(self) -> Entreprise:
        """Getter de l'attribut _entreprise.

        Returns:
            Entreprise: entreprise d'accueil
        """
        return self._entreprise

    @property
    def tuteur_pro(self) -> TuteurPro:
        """Getter de l'attribut _tuteur_pro.

        Returns:
            TuteurPro: tuteur professionnel
        """
        return self._tuteur_pro

    @property
    def tuteur_univ(self) -> TuteurUniv:
        """Getter de l'attribut _tuteur_univ.

        Returns:
            TuteurUniv: tuteur universitaire
        """
        return self._tuteur_univ

    @property
    def etudiant(self) -> Etudiant:
        """Getter de l'attribut _etudiant.

        Returns:
            Etudiant: étudiant
        """
        return self._etudiant

    # Setters

    @titre.setter
    def set_titre(self, titre_stg_alt):
        """Setter de l'attribut _titre.

        Args:
            titre_stg_alt (str): titre du stage ou de l'alternance
        """
        self._titre = titre_stg_alt

    @theme.setter
    def set_theme(self, theme_stg_alt):
        """Setter de l'attribut _theme.

        Args:
            theme_stg_alt (str): thème du stage ou de l'alternance
        """
        self._theme = theme_stg_alt

    @intitule.setter
    def set_intitule(self, intitule_stg_alt):
        """Setter de l'attribut _intitule.

        Args:
            intitule_stg_alt (str): intitulé du stage ou de l'alternance
        """
        self._intitule = intitule_stg_alt

    @dt_date_debut.setter
    def set_dt_date_debut(self, dt_date_debut_stg_alt):
        """Setter de l'attribut _dt_date_debut.

        Args:
            dt_date_debut_stg_alt (datetime): date de début du stage ou de l'alternance
        """
        self._dt_date_debut = dt_date_debut_stg_alt

    @dt_date_fin.setter
    def set_dt_date_fin(self, dt_date_fin_stg_alt):
        """Setter de l'attribut _dt_date_fin.

        Args:
            dt_date_fin_stg_alt (datetime): date de fin du stage ou de l'alternance
        """
        self._dt_date_fin = dt_date_fin_stg_alt

    @duree_entreprise.setter
    def set_duree_entreprise(self, duree_stg_alt):
        """Setter de l'attribut _duree.

        Args:
            duree_stg_alt (int): durée du stage ou de l'alternance
        """
        self._duree = duree_stg_alt

    @entreprise.setter
    def set_entreprise(self, entreprise):
        """Setter de l'attribut _entreprise.

        Args:
            entreprise (Entreprise): entreprise d'accueil
        """
        self._entreprise = entreprise

    @tuteur_pro.setter
    def set_tuteur_pro(self, tuteur_pro):
        """Setter de l'attribut _tuteur_pro.

        Args:
            tuteur_pro (TuteurPro): tuteur professionnel
        """
        self._tuteur_pro = tuteur_pro

    @tuteur_univ.setter
    def set_tuteur_univ(self, tuteur_univ):
        """Setter de l'attribut _tuteur_univ.

        Args:
            tuteur_univ (TuteurUniv): tuteur universitaire
        """
        self._tuteur_univ = tuteur_univ

    @etudiant.setter
    def set_etudiant(self, etudiant):
        """Setter de l'attribut _etudiant.

        Args:
            etudiant (Etudiant): étudiant
        """
        self._etudiant = etudiant

    def __str__(self) -> str:
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str: Représentation de l'objet sous forme de chaîne de caractères
        """
        return (
            "Stage ou alternance : "
            + self._titre
            + " ("
            + self._intitule
            + ") chez "
            + self._entreprise.nom
            + " du "
            + self._dt_date_debut
            + " au "
            + self._dt_date_fin
            + " avec "
            + self._tuteur_pro.nom
            + " et "
            + self._tuteur_univ.nom
            + " pour l'étudiant "
            + self._etudiant.nom
            + " "
            + self._etudiant.prenom
        )

    def __eq__(self, other: "StageAlt") -> bool:
        """Compare deux objets StageAlt.

        Args:
            other (StageAlt): Stage ou alternance à comparer

        Returns:
            bool: True si les objets sont identiques, False sinon
        """
        return self._id == other.id
