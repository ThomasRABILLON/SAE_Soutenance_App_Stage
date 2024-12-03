from common.models import Entreprise


class TuteurPro:
    """Classe représentant un tuteur professionnel."""

    def __init__(
        self,
        id_tut_pro: int,
        civilite_tut_pro: str,
        nom_tut_pro: str,
        prenom_tut_pro: str,
        tel_tut_pro: str,
        gsm_tut_pro: str,
        mail_tut_pro: str,
        entreprise: Entreprise,
    ):
        self._id = id_tut_pro
        self._civilite = civilite_tut_pro
        self._nom = nom_tut_pro
        self._prenom = prenom_tut_pro
        self._tel = tel_tut_pro
        self._gsm = gsm_tut_pro
        self._mail = mail_tut_pro
        self._entreprise = entreprise

    # Getters
    @property
    def id(self) -> int:
        """Obtient l'identifiant du tuteur professionnel.

        Returns:
            int: L'identifiant du tuteur professionnel.
        """

        return self._id

    @property
    def civilite(self) -> str:
        """Obtient la civilité du tuteur professionnel.

        Returns:
            str: La civilité du tuteur professionnel.
        """

        return self._civilite

    @property
    def nom(self) -> str:
        """Obtient le nom du tuteur professionnel.

        Returns:
            str: Le nom du tuteur professionnel.
        """

        return self._nom

    @property
    def prenom(self) -> str:
        """Obtient le prénom du tuteur professionnel.

        Returns:
            str: Le prénom du tuteur professionnel.
        """

        return self._prenom

    @property
    def tel(self) -> str:
        """Obtient le numéro de téléphone du tuteur professionnel.

        Returns:
            str: Le numéro de téléphone du tuteur professionnel.
        """

        return self._tel

    @property
    def gsm(self) -> str:
        """Obtient le numéro de téléphone portable du tuteur professionnel.

        Returns:
            str: Le numéro de téléphone portable du tuteur professionnel.
        """

        return self._gsm

    @property
    def mail(self) -> str:
        """Obtient l'adresse mail du tuteur professionnel.

        Returns:
            str: L'adresse mail du tuteur professionnel.
        """

        return self._mail

    @property
    def entreprise(self) -> Entreprise:
        """Obtient l'entreprise du tuteur professionnel.

        Returns:
            Entreprise: L'entreprise du tuteur professionnel.
        """
        return self._entreprise

    # Setters
    @civilite.setter
    def civilite(self, value: str) -> None:
        """Définit la civilité du tuteur professionnel

        Args:
            value (str): La civilité du tuteur professionnel.
        """
        self._civilite = value

    @nom.setter
    def nom(self, value: str) -> None:
        """Définit le nom du tuteur professionnel.

        Args:
            value (str): Le nom du tuteur professionnel.
        """

        self._nom = value

    @prenom.setter
    def prenom(self, value: str) -> None:
        """Définit le prénom du tuteur professionnel.

        Args:
            value (str): Le prénom du tuteur professionnel.
        """

        self._prenom = value

    @tel.setter
    def tel(self, value: str) -> None:
        """Définit le numéro de téléphone du tuteur professionnel.

        Args:
            value (str): Le numéro de téléphone du tuteur professionnel.
        """

        self._tel = value

    @gsm.setter
    def gsm(self, value: str) -> None:
        """Définit le numéro de téléphone portable du tuteur professionnel.

        Args:
            value (str): Le numéro de téléphone portable du tuteur professionnel.
        """

        self._gsm = value

    @mail.setter
    def mail(self, value: str) -> None:
        """Définit l'adresse mail du tuteur professionnel.

        Args:
            value (str): L'adresse mail du tuteur professionnel.
        """

        self._mail = value

    @entreprise.setter
    def entreprise(self, value: Entreprise) -> None:
        """Définit l'entreprise du tuteur professionnel.

        Args:
            value (Entreprise): L'entreprise du tuteur professionnel.
        """

        self._entreprise = value

    def __str__(self) -> str:
        return f"TuteurPro(id={self.id}, civilite={self.civilite}, nom={self.nom}, prenom={self.prenom}, tel={self.tel}, gsm={self.gsm}, mail={self.mail}, entreprise={self.entreprise})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: "TuteurPro") -> bool:
        return self.id == other.id
