class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """function recreating np.dot() btw to lists"""
        ret = sum([x * y for x, y in zip(V1, V2)])
        print("Dot product is:", ret)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """function to add value btw two lists"""
        ret = [float(x) + float(y) for x, y in zip(V1, V2)]
        print("Add Vector is :", ret)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """function to substract value btw two lists"""
        ret = [float(x) - float(y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", ret)
