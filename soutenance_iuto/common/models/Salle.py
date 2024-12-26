class Salle:
    """Classe Salle
    """

    def __init__(self, id_salle: int, nom_salle: str):
        """Constructeur de la classe Salle.

        Args:
            id_salle (int): id de la salle
            nom_salle (str): nom de la salle
        """
        self._id = id_salle
        self._nom = nom_salle

    #Getters
    @property
    def id(self) -> int:
        """Getter de l'attribut _id.

        Returns:
            int: id de la salle
        """
        return self._id

    @property
    def nom(self) -> str:
        """Getter de l'attribut _nom.

        Returns:
            str: nom de la salle
        """
        return self._nom

    #Setters

    @nom.setter
    def nom(self, nom):
        """Setter de l'attribut _nom.

        Args:
            nom (str): nom de la salle
        """
        self._nom = nom

    def __str__(self):
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str : Représentation de l'objet sous forme de chaîne de caractères
        """
        return f"{self._nom}"

    def __eq__(self, value: "Salle") -> bool:
        """Compare deux objets Salle.

        Args:
            value (Salle): Salle à comparer

        Returns:
            bool: True si les objets sont identiques, False sinon
        """
        return self.id == value.id
