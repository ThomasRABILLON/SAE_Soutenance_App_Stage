import json
import models.Entreprise

class EntrepriseSerializer:
    """Serializer pour la classe Entreprise."""

    def __init__(self, instance=None):
        """
        Initialise le serializer avec une instance d'Entreprise optionnelle.

        Args:
            instance (Entreprise, optional): Instance de la classe Entreprise à sérialiser.
        """
        self.instance = instance

    def to_dict(self):
        """
        Sérialise l'instance en un dictionnaire.

        Returns:
            dict: Données sérialisées.
        """
        if not self.instance:
            return {}

        return {
            "id": self.instance.id,
            "nom": self.instance.nom,
            "cp": self.instance.cp,
            "ville": self.instance.ville,
        }

    def to_json(self):
        """
        Sérialise l'instance en une chaîne JSON.

        Returns:
            str: Représentation JSON de l'instance.
        """
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(data):
        """
        Désérialise un dictionnaire en une instance d'Entreprise.

        Args:
            data (dict): Données en dictionnaire.

        Returns:
            Entreprise: Instance d'Entreprise créée.
        """
        return Entreprise(
            id_etp=data["id"],
            nom_etp=data["nom"],
            cp_etp=data["cp"],
            ville_etp=data["ville"]
        )

    @staticmethod
    def from_json(json_data):
        """
        Désérialise une chaîne JSON en une instance de Entreprise.

        Args:
            json_data (str): Chaîne JSON.

        Returns:
            Entreprise: Instance de Entreprise créée.
        """
        data = json.loads(json_data)
        return EntrepriseSerializer.from_dict(data)
