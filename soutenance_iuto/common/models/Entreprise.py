class Entreprise:
    """Classe représentant une entreprise."""

    def __init__(self, id_etp: int, nom_etp: str, cp_etp: str, ville_etp: str):
        self._id = id_etp
        self._nom = nom_etp
        self._cp = cp_etp
        self._ville = ville_etp

    # Getters
    @property
    def id(self) -> int:
        """Obtient l'identifiant de l'entreprise.

        Returns:
            int: L'identifiant de l'entreprise.
        """
        return self._id

    @property
    def nom(self) -> str:
        """Obtient le nom de l'entreprise.

        Returns:
            str: Le nom de l'entreprise.
        """
        return self._nom

    @property
    def cp(self) -> str:
        """Obtient le code postal de l'entreprise.

        Returns:
            str: Le code postal de l'entreprise.
        """
        return self._cp

    @property
    def ville(self) -> str:
        """Obtient la ville de l'entreprise.

        Returns:
            str: La ville de l'entreprise.
        """

        return self._ville

    # Setters
    @nom.setter
    def nom(self, value: str) -> None:
        """Définit le nom de l'entreprise.

        Args:
            value (str): Le nom de l'entreprise.
        """

        self._nom = value

    @cp.setter
    def cp(self, value: str) -> None:
        """Définit le code postal de l'entreprise.

        Args:
            value (str): Le code postal de l'entreprise.
        """

        self._cp = value

    @ville.setter
    def ville(self, value: str) -> None:
        """Définit la ville de l'entreprise.

        Args:
            value (str): La ville de l'entreprise.
        """

        self._ville = value

    def __str__(self) -> str:
        return f"Entreprise(id={self.id}, nom={self.nom}, cp={self.cp}, ville={self.ville})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: "Entreprise") -> bool:
        return self.id == other.id
