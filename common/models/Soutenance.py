from common.models import DateHoraire, Salle, StageAlt, Professeur


class Soutenance:
    """Classe représentant une soutenance de stage ou d'alternance.
    """
    def __init__(self, id_sout: int, stg_alt: StageAlt, horaire: DateHoraire, salle: Salle, prof_candide: Professeur):
        """Constructeur de la classe Soutenance.

        Args:
            id_sout (int): id de la soutenance
            stg_alt (StageAlt): stage ou alternance
            horaire (DateHoraire): date et horaire de la soutenance
            salle (Salle): salle de la soutenance
            prof_candide (Professeur): professeur candide
        """
        self._id = id_sout
        self._stage_alt = stg_alt
        self._horaire = horaire
        self._salle = salle
        self._prof_candide = prof_candide
    
    # Getters
    @property
    def id(self) -> int:
        """Getter de l'attribut _id.

        Returns:
            int: id de la soutenance
        """
        return self._id
    
    @property
    def stage_alt(self) -> StageAlt:
        """Getter de l'attribut _stage_alt.

        Returns:
            StageAlt: stage ou alternance
        """
        return self._stage_alt
    
    @property
    def horaire(self) -> DateHoraire:
        """Getter de l'attribut _horaire.

        Returns:
            DateHoraire: date et horaire de la soutenance
        """
        return self._horaire
    
    @property
    def salle(self) -> Salle:
        """Getter de l'attribut _salle.

        Returns:
            Salle: salle de la soutenance
        """
        return self._salle
    
    @property
    def prof_candide(self) -> Professeur:
        """Getter de l'attribut _prof_candide.

        Returns:
            Professeur: professeur candide
        """
        return self._prof_candide
    
    # Setters
    @stage_alt.setter
    def stage_alt(self, stage_alt):
        """Setter de l'attribut _stage_alt.

        Args:
            stage_alt (StageAlt): stage ou alternance
        """
        self._stage_alt = stage_alt
        
    @horaire.setter
    def horaire(self, horaire):
        """Setter de l'attribut _horaire.

        Args:
            horaire (DateHoraire): date et horaire de la soutenance
        """
        self._horaire = horaire
        
    @salle.setter
    def salle(self, salle):
        """Setter de l'attribut _salle.

        Args:
            salle (Salle): salle de la soutenance
        """
        self._salle = salle
        
    @prof_candide.setter
    def prof_candide(self, prof_candide):
        """Setter de l'attribut _prof_candide.

        Args:
            prof_candide (Professeur): professeur candide de la soutenance
        """
        self._prof_candide = prof_candide
        
    def __str__(self):
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str : Représentation de l'objet sous forme de chaîne de caractères
        """
        return f"{self._stage_alt} {self._horaire} {self._salle} {self._prof_candide}"
    
    def __eq__(self, value: "Soutenance") -> bool:
        """Compare deux objets Soutenance.

        Args:
            value (Soutenance): Soutenance à comparer

        Returns:
            bool: True si les objets sont identiques, False sinon
        """
        return self._id == value.id