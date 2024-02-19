from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        return (f"{self.family_name}, {self.eyes}, {self.hairs}")


    def __repr__(self) -> str:
        return (f"{self.family_name}, {self.eyes}, {self.hairs}")


    def die(self):
         self.is_alive = False


class Lannister(Character):
        """Representing the Lannister family"""
        def __init__(self, first_name: str, is_alive: bool = True):
            super().__init__(first_name, is_alive)
            self.family_name = "Lannister"
            self.eyes = "blue"
            self.hairs = "light"

        def __str__(self) -> str:
            return (f"{self.family_name}, {self.eyes}, {self.hairs}")


        def __repr__(self) -> str:
            return (f"{self.family_name}, {self.eyes}, {self.hairs}")


        def die(self):
            self.is_alive = False

        def create_lannister(first_name: str, is_alive: bool = True):
            return(Lannister(first_name, is_alive))