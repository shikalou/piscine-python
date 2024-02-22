class calculator:

    def __init__(self, obj: list[int]) -> None:
        """calculator class constructor"""
        self.vec = obj

    def __add__(self, object: int) -> None:
        """overload operator '+'"""
        self.vec = [x + object for x in self.vec]
        print(self.vec)

    def __mul__(self, object: int) -> None:
        """overload operator '*'"""
        self.vec = [x * object for x in self.vec]
        print(self.vec)

    def __sub__(self, object: int) -> None:
        """overload operator '-'"""
        self.vec = [x - object for x in self.vec]
        print(self.vec)

    def __truediv__(self, obj: int) -> None:
        """overload operator '/'"""
        self.vec = [x / obj if obj else print("no div by 0") for x in self.vec]
        print(self.vec)
