import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from load_image import ft_load


def ft_rotate(img: np.ndarray) -> np.ndarray:
    # ret = np.transpose(img)
    a = np.array([[1, 2, 3], [4, 5, 6]])
    width, height = a.shape[1], a.shape[0]
    print(width, height, np.shape(a))
    ret = []
    new_row=[]
    for column in range(0, height):
        for row in range(0, width):
            new_row.append(a[row][column])
        ret.append(new_row)
        new_row = []
    print(ret)
    print("New shape after Transpose:", np.shape(a))
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
    # print(rot_img)
    # plt.imshow(rot_img, cmap='gray')
    # plt.show()


if __name__ == "__main__":
    main()
