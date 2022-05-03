# Description: This is a sample of creating and drawing some color to an image

from math import dist
import cv2

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

image_size = [780, 780]

blank_img = np.ones( shape = (image_size[0], image_size[1], 3) )

blank_img[0][0] = (0,0,0)
blank_img[1][1] = (0,0,0)
blank_img[2][2] = (0,0,0)
blank_img[3][3] = (0,0,0)
blank_img[4][4] = (0,0,0)


center = (128, 128)
radius = 50
color = mcolors.to_rgb('red')

for pixel_x in range(center[0] - radius, center[0] + radius):
    if pixel_x > image_size[0]:
        continue

    for pixel_y in range(center[0] - radius, center[1] + radius):
        if pixel_y > image_size[1]:
            continue
        if dist( center, [pixel_x, pixel_y] ) < radius:
            blank_img[pixel_x][pixel_y] = color

plt.imshow(blank_img)
plt.show()