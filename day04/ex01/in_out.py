def square(x: int | float) -> int | float:
    """function to calculate the square of argument"""
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """function to calculate the exponentiation of argument"""
    return (x ** x)


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal x
        x = function(x)
        return (x)
    return (inner)
