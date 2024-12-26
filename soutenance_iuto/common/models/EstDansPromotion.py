from common.models import Etudiant, Promotion


class EstDansPromotion:
    """Classe représentant un étudiant dans une promotion."""

    def __init__(self, etudiant: Etudiant, promotion: Promotion):
        self._etudiant = etudiant
        self._promotion = promotion

    # Getters
    @property
    def etudiant(self) -> Etudiant:
        """Obtient l'étudiant dans la promotion.

        Returns:
            Etudiant: L'étudiant dans la promotion.
        """

        return self._etudiant

    @property
    def promotion(self) -> Promotion:
        """Obtient la promotion dans laquelle l'étudiant est.

        Returns:
            Promotion: La promotion dans laquelle l'étudiant est.
        """

        return self._promotion

    # Setters
    @etudiant.setter
    def etudiant(self, value: Etudiant) -> None:
        """Définit l'étudiant dans la promotion.

        Args:
            value (Etudiant): L'étudiant dans la promotion.
        """

        self._etudiant = value

    @promotion.setter
    def promotion(self, value: Promotion) -> None:
        """Définit la promotion dans laquelle l'étudiant est.

        Args:
            value (Promotion): La promotion dans laquelle l'étudiant est.
        """
        
        self._promotion = value

    def __str__(self) -> str:
        return f"EstDansPromotion(etudiant={self.etudiant}, promotion={self.promotion})"

    def __repr__(self) -> str:
        return str(self)
