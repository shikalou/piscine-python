import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> any:
    """
    function that loads an image, print its shape and
    its pixels content in RGB format
    """
    try:
        assert type(path) is str, "need img path in a str"
        img = plt.imread(path)
        print(f"the shape of the image is: {np.shape(img)}")
        return (img)
    except Exception as msg:
        print(msg)
