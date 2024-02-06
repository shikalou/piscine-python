import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv



def ft_reshape(img: np.ndarray, dim: tuple) -> any:
    """
    reshape and return img
    img is a numpy nd.array and dim is a tuple with
    value to crop
    """
    width, height = img.shape[1], img.shape[0]
    crop_width = dim[0] if dim[0] < width else width
    crop_height = dim[1] if dim[1] < height else height
    mid_x, mid_y = int(width/2), int(height/2)
    cw2, ch2 = int(crop_width/2), int(crop_height/2)
    crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
    return (crop_img)


def ft_load(path: str) -> any:
    """
    function that loads an image, print its shape and
    its pixels content after zoom in gray format
    """
    try:
        assert type(path) is str, "need img path in a str"
        img = plt.imread(path)
        # plt.imshow(img)
        # plt.show()
        zoomed_img = ft_reshape(img, (400, 400))
        gray = cv.cvtColor(zoomed_img, cv.COLOR_RGB2GRAY)
        print("The shape of the image is:", np.shape(gray))
        print(gray)
        return (gray)
    except AssertionError as msg:
        print("AssertionError:", msg)
        return(None)
    except Exception as msg:
        print(msg)
        return (None)
