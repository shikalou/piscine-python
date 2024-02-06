import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


def ft_load(path: str) -> any:
    """
    function that loads an image, print its shape and
    its pixels content in RGB format
    """
    try:
        assert type(path) is str, "need img path in a str"
        img = plt.imread(path)
        print("The shape of the image is:", np.shape(img))
        # plt.imshow(img)
        # plt.show()
        return (img)
    except AssertionError as msg:
        print("AssertionError:", msg)
    except Exception as msg:
        print(msg)
        return (None)
