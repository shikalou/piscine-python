def mean(args: tuple) -> any:
    """function to calculate mean"""
    if (not len(args)):
        return ("ERROR")
    return (sum(args) / len(args))


def med(args: tuple) -> any:
    """function to calculate mediane"""
    if (not len(args)):
        return ("ERROR")
    if len(args) % 2 != 0:
        sorte = sorted(args)
        ret = sorte[int(len(sorte)/2)]
    else:
        first = len(args) // 2 - 1
        second = len(args) // 2
        ret = mean(tuple((args[first], args[second])))
    return (ret)


def quar(args: tuple) -> any:
    """function to calculate lower and upper quartiles"""
    if (not len(args)):
        return ("ERROR")
    sorte = sorted(args)
    low = float(sorte[int((len(sorte)) / 4)])
    high = float(sorte[int(((len(sorte)) * (3 / 4)))])
    ret = [low, high]
    return (ret)


def std(args: tuple) -> any:
    """function to calculate standart deviance"""
    if (not len(args)):
        return ("ERROR")
    mea = mean(args)
    calc = [x - mea for x in args]
    total = [x ** 2 for x in calc]
    mea = mean(total)
    return (mea ** 0.5)


def var(args: tuple) -> any:
    """function to calculate variance"""
    if (not len(args)):
        return ("ERROR")
    mea = mean(args)
    total = sum([(x - mea) ** 2 for x in args])
    return (total / len(args))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """def ft_statistics(*args: any, **kwargs: any) -> None"""
    if (args):
        if (not all([isinstance(i, (float, int)) for i in args])):
            print("problems with args")
            return

    for key, value in kwargs.items():
        if value == "mean":
            print("mean :", mean(args))
        elif value == "median":
            print("median :", med(args))
        elif value == "quartile":
            print("quartile :", quar(args))
        elif value == "std":
            print("std :", std(args))
        elif value == "var":
            print("var :", var(args))
        else:
            pass

# https://www.programiz.com/python-programming/args-and-kwargs
