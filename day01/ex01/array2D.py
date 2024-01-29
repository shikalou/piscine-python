import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        assert type(family) is list, "wrong array type"
        tab = np.array(family)
        print(f"my shape is : {tab.shape}")
        tab = tab[start:end]
        print(f"my new shap is : {tab.shape}")
    except AssertionError as msg:
        print(msg)
    return (tab)
