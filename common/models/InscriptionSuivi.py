from common.models import StageAlt, Professeur


class InscriptionSuivi:
    """Classe représentant une inscription à un suivi de stage alterné.
    """
    
    def __init__(self, stg_alt: StageAlt, prof: Professeur):
        """Constructeur de la classe InscriptionSuivi.

        Args:
            stg_alt (StageAlt): Stage ou alternance
            prof (Professeur): Professeur responsable du suivi
        """
        self._stg_alt = stg_alt
        self._prof = prof
    
    # Getters
    @property
    def stg_alt(self) -> StageAlt:
        """Getter de l'attribut stg_alt.

        Returns:
            StageAlt: Stage ou alternance
        """
        return self._stg_alt
    
    @property
    def prof(self) -> Professeur:
        """Getter de l'attribut prof.

        Returns:
            Professeur: Professeur responsable du suivi
        """
        return self._prof
    
    # Setters
    @stg_alt.setter
    def stg_alt(self, stg_alt):
        """Setter de l'attribut stg_alt.

        Args:
            stg_alt (StageAlt): Stage ou alternance
        """
        self._stg_alt = stg_alt
        
    @prof.setter
    def prof(self, prof):
        """Setter de l'attribut prof.

        Args:
            prof (Professeur): Professeur responsable du suivi
        """
        self._prof = prof
        
    def __str__(self):
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str : Représentation de l'objet sous forme de chaîne de caractères
        """
        return f"{self._stg_alt} {self._prof}"
    
    def __eq__(self, value: "InscriptionSuivi") -> bool:
        """Compare deux objets InscriptionSuivi.

        Args:
            value (InscriptionSuivi): InscriptionSuivi

        Returns:
            bool: True si les deux objets sont égaux, False sinon
        """
        return self.stg_alt == value.stg_alt and self._prof == value.prof