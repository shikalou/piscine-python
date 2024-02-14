import pandas as pd


def load(path: str) -> pd.dataFrame:
    """
    def load(path: str) -> pd.dataFrame
    function that loads a cvs file in a pd.dataFrame object
    """
    ret = pd.read_csv(path)
    print("Loading dataset of dimensions", ret.shape)
    return (ret)
