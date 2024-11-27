class Professeur:
    """Classe représentant un professeur."""

    def __init__(
        self,
        id_prof: int,
        num_prof: str,
        civilite_prof: str,
        nom_prof: str,
        prenom_prof: str,
        mail_prof: str,
    ):
        self._id = id_prof
        self._num = num_prof
        self._civilite = civilite_prof
        self._nom = nom_prof
        self._prenom = prenom_prof
        self._mail = mail_prof

    # Getters
    @property
    def id(self) -> int:
        """Obtient l'identifiant du professeur.

        Returns:
            int: L'identifiant du professeur.
        """

        return self._id

    @property
    def num(self) -> str:
        """Obtient le numéro du professeur.

        Returns:
            str: Le numéro du professeur.
        """

        return self._num

    @property
    def civilite(self) -> str:
        """Obtient la civilité du professeur.

        Returns:
            str: La civilité du professeur.
        """

        return self._civilite

    @property
    def nom(self) -> str:
        """Obtient le nom du professeur.

        Returns:
            str: Le nom du professeur.
        """

        return self._nom

    @property
    def prenom(self) -> str:
        """Obtient le prénom du professeur.

        Returns:
            str: Le prénom du professeur.
        """

        return self._prenom

    @property
    def mail(self) -> str:
        """Obtient le mail du professeur.

        Returns:
            str: Le mail du professeur.
        """

        return self._mail

    # Setters
    @num.setter
    def num(self, value: str) -> None:
        """Définit le numéro du professeur.

        Args:
            value (str): Le numéro du professeur.
        """

        self._num = value

    @civilite.setter
    def civilite(self, value: str) -> None:
        """Définit la civilité du professeur.

        Args:
            value (str): La civilité du professeur.
        """

        self._civilite = value

    @nom.setter
    def nom(self, value: str) -> None:
        """Définit le nom du professeur.

        Args:
            value (str): Le nom du professeur.
        """

        self._nom = value

    @prenom.setter
    def prenom(self, value: str) -> None:
        """Définit le prénom du professeur.

        Args:
            value (str): Le prénom du professeur.
        """

        self._prenom = value

    @mail.setter
    def mail(self, value: str) -> None:
        """Définit le mail du professeur.

        Args:
            value (str): Le mail du professeur.
        """

        self._mail = value

    def __str__(self) -> str:
        return f"Professeur(id={self.id}, num={self.num}, civilite={self.civilite}, nom={self.nom}, prenom={self.prenom}, mail={self.mail})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: "Professeur") -> bool:
        return self.id == other.id
