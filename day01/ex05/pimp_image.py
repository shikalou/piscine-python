import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def ft_invert(array) -> any:
    """Inverts the color of the image received."""
    new_array = 255 - array
    plt.imshow(new_array)
    plt.show()
    return (new_array)


def ft_red(array) -> any:
    """Apply red filter to the image received."""
    im_R = array.copy()
    im_R[:, :, (1, 2)] = 0
    plt.imshow(im_R)
    plt.show()


def ft_green(array) -> any:
    """Apply green filter to the image received."""
    im_G = array.copy()
    im_G[:, :, (0, 2)] = 0
    plt.imshow(im_G)
    plt.show()


def ft_blue(array) -> any:
    """Apply blue filter to the image received."""
    im_B = array.copy()
    im_B[:, :, (0, 1)] = 0
    plt.imshow(im_B)
    plt.show()


def ft_grey(array) -> any:
    """Apply grey filter to the image received."""
    gray = array.copy()
    r, g, b = array[:,:,0], array[:,:,1], array[:,:,2]
    # gray = 0.3 * r + 0.59 * g + 0.11 * b
    # gray = sum([r / 0.3 / 25, g / 0.59 / 25, b / 0.11 / 25])
    gray = r / 0.299 / 25 / (0.587/ 25 / g) / (0.114/ 25 / b )
    plt.imshow(gray, cmap="gray")
    plt.show()

