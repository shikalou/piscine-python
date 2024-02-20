class calculator:

    def __init__(self, obj: list[int]) -> None:
        self.vec = obj

    def __add__(self, object: int) -> None:
        self.vec = [x + object for x in self.vec]
        print(self.vec)
    def __mul__(self, object: int) -> None:
        self.vec = [x * object for x in self.vec]
        print(self.vec)
    def __sub__(self, object: int) -> None:
        self.vec = [x - object for x in self.vec]
        print(self.vec)
    def __truediv__(self, object: int) -> None:
        self.vec = [x / object for x in self.vec if object]
        print(self.vec)