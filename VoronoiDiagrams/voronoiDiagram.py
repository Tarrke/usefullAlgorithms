# Description: atempt to make a simple Voronoi diagram from a random distribution of points

from math import dist
import random
import cv2

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def draw_point(img, x, y, color):
    """Draw a 'point' in a smal cross shape at coordinates"""
    #for pixel in ((x, y), (x-1, y), (x+1, y), (x, y+1), (x, y-1)):
        #if pixel[0] > 


nb_points = 40
image_size = (400, 400)

# Creating a blank image
img = np.ones( shape = (image_size[0], image_size[1], 3) )

# Generating the random points
for pt in range(nb_points):
    pt_x = random.randrange(0, image_size[0])
    pt_y = random.randrange(0, image_size[1])

    draw_point(img, pt_x, pt_y)

plt.imshow(img)
plt.show()