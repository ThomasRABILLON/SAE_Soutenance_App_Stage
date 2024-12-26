class Secretaire:
    """Classe Secretaire
    """

    def __init__(self, id_sec: int, nom_sec: str, prenom_sec: str, email_sec: str):
        """Constructeur de la classe Secretaire.

        Args:
            id_sec (int): id du secrétaire
            nom_sec (str): nom du secrétaire
            prenom_sec (str): prénom du secrétaire
            email_sec (str): email du secrétaire
        """
        self._id = id_sec
        self._nom = nom_sec
        self._prenom = prenom_sec
        self._email = email_sec

    # Getters
    @property
    def id(self) -> int:
        """Getter de l'attribut _id.

        Returns:
            int: id du secrétaire
        """
        return self._id

    @property
    def nom(self) -> str:
        """Getter de l'attribut _nom.

        Returns:
            str: nom du secrétaire
        """
        return self._nom

    @property
    def prenom(self) -> str:
        """Getter de l'attribut _prenom.

        Returns:
            str: prénom du secrétaire
        """
        return self._prenom

    @property
    def email(self) -> str:
        """Getter de l'attribut _email.

        Returns:
            str: email du secrétaire
        """
        return self._email

    # Setters
    @nom.setter
    def nom(self, nom):
        """Setter de l'attribut _nom.

        Args:
            nom (str): nom du secrétaire
        """
        self._nom = nom

    @prenom.setter
    def prenom(self, prenom):
        """Setter de l'attribut _prenom.

        Args:
            prenom (str): prenom du secrétaire
        """
        self._prenom = prenom

    @email.setter
    def email(self, email):
        """Setter de l'attribut _email.

        Args:
            email (str): email du secrétaire
        """
        self._email = email

    def __str__(self):
        """Renvoie une représentation de l'objet sous forme de chaîne de caractères

        Returns:
            str : Représentation de l'objet sous forme de chaîne de caractères
        """
        return f"{self._nom} {self._prenom} {self._email}"

    def __eq__(self, value: "Secretaire") -> bool:
        """Compare deux objets Secretaire.

        Args:
            value (Secretaire): Secretaire à comparer

        Returns:
            bool: True si les objets sont identiques, False sinon
        """
        return self.id == value.id
