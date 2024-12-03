import datetime
import time

class DateHoraire:
    """Date et Horaire d'une soutenance
    """

    def __init__(self, id_date_horaire: int, dt_date: datetime, horaire: time, duree: int):
        """Constructeur de la classe DateHoraire

        Args:
            id_date_horaire (int): id de l'horaire
            dt_date (datetime): date
            horaire (time): horaire
            duree (int): durée
        """
        self._id = id_date_horaire
        self._date = dt_date
        self._horaire = horaire
        self._duree = duree

    def __str__(self) -> str:
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str: Représentation de l'objet sous forme
        """
        return f"{self._date} {self._horaire} {self._duree}"

    def __eq__(self, value: "DateHoraire") -> bool:
        """Compare deux objets DateHoraire
        """
        return self._id == value.id
