import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from load_image import ft_load


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


def main():
    """
    display shape and zoomed version of an image
    """
    img = ft_load("animal.jpeg")
    if (img is None):
        sys.exit(1)
    print(img)
    zoomed_img = ft_reshape(img, (400, 400))
    gray = cv.cvtColor(zoomed_img, cv.COLOR_RGB2GRAY)
    print("New shape after slicing:", np.shape(gray))
    print(gray)
    plt.imshow(gray, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
