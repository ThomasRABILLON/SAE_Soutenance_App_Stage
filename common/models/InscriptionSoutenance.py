from common.models import Soutenance, Professeur


class InscriptionSoutenance:
    """Modele de l'inscription d'un prof à une soutenance
    """
    
    def __init__(self, soutenance: Soutenance, prof: Professeur):
        """Constructeur de la classe InscriptionSoutenance

        Args:
            soutenance (Soutenance): Soutenance
            prof (Professeur): Professeur
        """
        self._soutenance = soutenance
        self._prof = prof
        
    # Getters
    @property
    def soutenance(self) -> Soutenance:
        """Renvoie la soutenance

        Returns:
            Soutenance: Soutenance
        """
        return self._soutenance
    
    @property
    def prof(self) -> Professeur:
        """ Renvoie le prof

        Returns:
            Professeur: Professeur
        """
        return self._prof
    
    # Setters
    @soutenance.setter
    def soutenance(self, soutenance):
        """Définit la soutenance

        Args:
            soutenance (Soutenance): Soutenance
        """
        self._soutenance = soutenance
        
    @prof.setter
    def prof(self, prof):
        """Définit le prof

        Args:
            prof (Prof): Professeur
        """
        self._prof = prof
        
    def __str__(self):
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str: Représentation de l'objet sous forme
        """
        return f"{self._soutenance} {self._prof}"
    
    def __eq__(self, value: "InscriptionSoutenance") -> bool:
        """Compare deux objets InscriptionSoutenance

        Args:
            value (InscriptionSoutenance): InscriptionSoutenance

        Returns:
            bool: True si les deux objets sont égaux, False sinon
        """
        return self.soutenance == value.soutenance and self._prof == value.prof