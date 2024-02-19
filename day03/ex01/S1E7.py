from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon class construtor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """The __str__() method returns a human-readable, or informal,
        string representation of an object."""
        return (f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")

    def __repr__(self) -> str:
        """The __repr__() method returns a more information-rich,
        or official, string representation of an object."""
        return (f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")

    def die(self):
        """function to change is_alive state to False"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """The __str__() method returns a human-readable, or informal,
        string representation of an object."""
        return (f"{self.family_name}, {self.eyes}, {self.hairs}")

    def __repr__(self) -> str:
        """The __repr__() method returns a more information-rich,
        or official, string representation of an object."""
        return (f"{self.family_name}, {self.eyes}, {self.hairs}")

    def die(self):
        """function to change is_alive state to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """class method to create a characters in a chain"""
        return (cls(first_name, is_alive))
