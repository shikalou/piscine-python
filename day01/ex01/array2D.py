import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    a function that takes a 2D array as a parameter and return a trucated
    version of the array based on the provided start and end arguments
    using the slicing method.
    """
    try:
        assert type(family) is list, "wrong array type"
        assert type(start) is int, "need int as start"
        assert type(end) is int, "need int as end"
        print(f"my shape is : {np.shape(family)}")
        family = family[start:end]
        print(f"my new shap is : {np.shape(family)}")
        return (family)
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit(1)
    except Exception as msg:
        print(msg)
        exit(1)
