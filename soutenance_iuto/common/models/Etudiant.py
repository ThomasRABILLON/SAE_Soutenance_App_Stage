class Etudiant:
    """Classe représentant un étudiant."""

    def __init__(
        self,
        id_etu: int,
        num_etu: str,
        ine_etu: str,
        civilite_etu: str,
        nom_etu: str,
        prenom_etu: str,
        mail_etu: str,
        alternant: bool,
    ):
        self._id = id_etu
        self._num = num_etu
        self._ine = ine_etu
        self._civilite = civilite_etu
        self._nom = nom_etu
        self._prenom = prenom_etu
        self._mail = mail_etu
        self._alternant = alternant

    # Getters
    @property
    def id(self) -> int:
        """Obtient l'identifiant de l'étudiant.

        Returns:
            int: L'identifiant de l'étudiant.
        """

        return self._id

    @property
    def num(self) -> str:
        """Obtient le numéro de l'étudiant.

        Returns:
            str: Le numéro de l'étudiant.
        """

        return self._num

    @property
    def ine(self) -> str:
        """Obtient l'INE de l'étudiant.

        Returns:
            str: L'INE de l'étudiant.
        """

        return self._ine

    @property
    def civilite(self) -> str:
        """Obtient la civilité de l'étudiant.

        Returns:
            str: La civilité de l'étudiant.
        """

        return self._civilite

    @property
    def nom(self) -> str:
        """Obtient le nom de l'étudiant.

        Returns:
            str: Le nom de l'étudiant.
        """

        return self._nom

    @property
    def prenom(self) -> str:
        """Obtient le prénom de l'étudiant.

        Returns:
            str: Le prénom de l'étudiant.
        """

        return self._prenom

    @property
    def mail(self) -> str:
        """Obtient le mail de l'étudiant.

        Returns:
            str: Le mail de l'étudiant.
        """

        return self._mail

    @property
    def alternant(self) -> bool:
        """Obtient si l'étudiant est un alternant.

        Returns:
            bool: Si l'étudiant est un alternant.
        """

        return self._alternant

    # Setters
    @num.setter
    def num(self, value: str) -> None:
        """Définit le numéro de l'étudiant.

        Args:
            value (str): Le numéro de l'étudiant.
        """

        self._num = value

    @ine.setter
    def ine(self, value: str) -> None:
        """Définit l'INE de l'étudiant.

        Args:
            value (str): L'INE de l'étudiant.
        """

        self._ine = value

    @civilite.setter
    def civilite(self, value: str) -> None:
        """Définit la civilité de l'étudiant.

        Args:
            value (str): La civilité de l'étudiant.
        """

        self._civilite = value

    @nom.setter
    def nom(self, value: str) -> None:
        """Définit le nom de l'étudiant.

        Args:
            value (str): Le nom de l'étudiant.
        """

        self._nom = value

    @prenom.setter
    def prenom(self, value: str) -> None:
        """Définit le prénom de l'étudiant.

        Args:
            value (str): Le prénom de l'étudiant.
        """

        self._prenom = value

    @mail.setter
    def mail(self, value: str) -> None:
        """Définit le mail de l'étudiant.

        Args:
            value (str): Le mail de l'étudiant.
        """

        self._mail = value

    @alternant.setter
    def alternant(self, value: bool) -> None:
        """Définit si l'étudiant est un alternant.

        Args:
            value (bool): Si l'étudiant est un alternant.
        """

        self._alternant = value

    def __str__(self) -> str:
        return f"Etudiant(id={self.id}, num={self.num}, ine={self.ine}, civilite={self.civilite}, nom={self.nom}, prenom={self.prenom}, mail={self.mail}, alternant={self.alternant})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: "Etudiant") -> bool:
        return self.id == other.id
