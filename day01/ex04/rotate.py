import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from load_image import ft_load


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """
    rotate the 2d array like the transpose function
    """
    width, height = img.shape[1], img.shape[0]
    ret = []
    new_row = []
    i = 0
    while i < width:
        for row in img:
            new_row.append(row[i])
        i+=1
        ret.append(new_row)
        new_row = []
    print("New shape after Transpose:", np.shape(ret))
    ret = np.reshape(ret, (400, 400))
    return(ret)

def main():
    """
    display rotated version of an image
    """
    img = ft_load("animal.jpeg")
    if (img is None):
        sys.exit(1)
    print(img)
    rot_img = ft_rotate(img)
    print(rot_img)
    plt.imshow(rot_img, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
