from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """long live the fake king"""
    # def __init__(self, first_name: str, is_alive: bool = True):
    #     super().__init__(first_name, is_alive)

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

    def get_eyes(self) -> str:
        """getter for eyes attributs"""
        return (self.eyes)

    def get_hairs(self) -> str:
        """getter for hairs attributs"""
        return (self.hairs)

    def set_eyes(self, color: str):
        """setter for eyes attributs"""
        self.eyes = color

    def set_hairs(self, color: str):
        """setter for hairs attributs"""
        self.hairs = color
