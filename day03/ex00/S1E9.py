from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Character class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """docstring for init"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die():
        """change live state is_alive to False"""
        pass


class Stark(Character):
    """Stark class, takes Character object"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Stark Class constructor called"""
        super().__init__(first_name, is_alive)

    def die(self):
        """def die(self):
change object Character live state from True to False"""
        self.is_alive = False
