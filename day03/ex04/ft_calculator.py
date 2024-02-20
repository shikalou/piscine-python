class calculator:
    
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        ret = sum([x * y for x, y in zip(V1, V2)])
        print(ret)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        ret = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(ret)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        ret = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(ret)
