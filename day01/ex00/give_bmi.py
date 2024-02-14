def give_bmi(h: list[int | float], w: list[int | float]) \
            -> list[int | float]:
    """
    give_bmi(h: list[int | float], w: list[int | float])
        -> list[int | float]
    takes two list and return a list of bmi value
    """
    try:
        assert all([isinstance(i, (float, int)) for i in h]), "need int/float"
        assert all([isinstance(i, (float, int)) for i in w]), "need int/float"
        assert len(h) == len(w), "tabs size not the same"
        ret = [w/h**2 for w, h in zip(w, h)]
        return (ret)
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(0)
    except Exception as msg:
        print(msg)
        exit(0)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    takes a list and an int, and returns a list of booleans (True
    if above the limit).
    """
    try:
        assert all([isinstance(i, (float, int)) for i in bmi]), "not int/float"
        assert type(limit) is int, "limit can be int only"
        ret = [i > limit for i in bmi]
        return (ret)
    except AssertionError as msg:
        print(msg)
        exit(0)
    except Exception as msg:
        print(msg)
        exit(0)