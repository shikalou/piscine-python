from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """long live the fake king"""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
    
    def set_eyes(color: str):
        