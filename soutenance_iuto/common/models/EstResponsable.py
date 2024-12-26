from common.models import Professeur, Promotion


class EstResponsable:
    """Classe représentant un responsable de promotion."""

    def __init__(self, professeur: Professeur, promotion: Promotion):
        self.professeur = professeur
        self.promotion = promotion

    # Getters
    @property
    def professeur(self) -> Professeur:
        """Obtient le professeur responsable de la promotion.

        Returns:
            Professeur: Le professeur responsable de la promotion.
        """

        return self.__professeur

    @property
    def promotion(self) -> Promotion:
        """Obtient la promotion dont le professeur est responsable.

        Returns:
            Promotion: La promotion dont le professeur est responsable.
        """

        return self.__promotion

    # Setters
    @professeur.setter
    def professeur(self, professeur: Professeur):
        """Définit le professeur responsable de la promotion.

        Args:
            professeur (Professeur): Le professeur responsable de la promotion.
        """

        self.__professeur = professeur

    @promotion.setter
    def promotion(self, promotion: Promotion):
        """Définit la promotion dont le professeur est responsable.

        Args:
            promotion (Promotion): La promotion dont le professeur est responsable.
        """

        self.__promotion = promotion

    def __str__(self):
        return (
            f"EstResponsable(professeur={self.professeur}, promotion={self.promotion})"
        )

    def __repr__(self):
        return str(self)
