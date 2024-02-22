import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    def load(path: str) -> pd.dataFrame
    function that loads a cvs file in a pd.dataFrame object
    """
    try:
        ret = pd.read_csv(path)
        print("Loading dataset of dimensions", ret.shape)
        return (ret)
    except Exception as msg:
        print(msg)
        return (None)
