import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(first: str, last: str) -> str:
    return (first[0]+last)


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = generate_login(self.name, self.surname)
        self.id = generate_id()

# field(init=false) permet de postpone l'init de la variable vu que j'ai
# besoin d'acceder a name et surname après leur init
