class Promotion:
    """Classe représentant une promotion."""

    def __init__(self, id_promo: int, annee_promo: int, filiere_promo: str):
        self._id = id_promo
        self._annee = annee_promo
        self._filiere = filiere_promo

    # Getters
    @property
    def id(self) -> int:
        """Obtient l'identifiant de la promotion.

        Returns:
            int: L'identifiant de la promotion.
        """

        return self._id

    @property
    def annee(self) -> int:
        """Obtient l'année de la promotion.

        Returns:
            int: L'année de la promotion.
        """

        return self._annee

    @property
    def filiere(self) -> str:
        """Obtient la filière de la promotion.

        Returns:
            str: La filière de la promotion.
        """

        return self._filiere

    # Setters
    @annee.setter
    def annee(self, value: int) -> None:
        """Définit l'année de la promotion.

        Args:
            value (int): L'année de la promotion.
        """

        self._annee = value

    @filiere.setter
    def filiere(self, value: str) -> None:
        """Définit la filière de la promotion.

        Args:
            value (str): La filière de la promotion.
        """
        
        self._filiere = value

    def __str__(self) -> str:
        return f"Promotion(id={self.id}, annee={self.annee}, filiere={self.filiere})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: "Promotion") -> bool:
        return self.id == other.id
