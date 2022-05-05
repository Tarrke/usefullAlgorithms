# Description: atempt to make a simple Voronoi diagram from a random distribution of points

from math import dist
import random
import cv2

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import sys

def draw_circle(img, x, y, radius, color):
    for pixel_x in range(x - radius, x + radius):
        if pixel_x >= len(img) or pixel_x < 0:
            continue

        for pixel_y in range(y - radius, y + radius):
            if pixel_y >= len(img[0]) or pixel_y < 0:
                continue
            if dist( [x, y], [pixel_x, pixel_y] ) < radius:
                img[pixel_x][pixel_y] = color

def draw_point(img, x, y, color):
    """Draw a 'point' in a smal cross shape at coordinates"""
    #for pixel in ((x, y), (x-1, y), (x+1, y), (x, y+1), (x, y-1)):
        #if pixel[0] > 

def random_color():
    return (random.randrange(0,255)/255.0, random.randrange(0,255)/255.0, random.randrange(0,255)/255.0)

nb_points = 40
image_size = (400, 600)

# Creating a blank image
img = np.ones( shape = (image_size[0], image_size[1], 3) )

generators = []
min_distance = 50

# Generating the random points
for pt in range(nb_points):
    pt_x = random.randrange(0, image_size[0])
    pt_y = random.randrange(0, image_size[1])

    # Check the distance to any point in the generators yet to be less than threshold
    if len(generators):
        m_distance = min([ dist([pt_x, pt_y], i[0]) for i in generators ])
        print(m_distance)
        if m_distance >= min_distance:
            generators.append([(pt_x, pt_y), random_color()])
    else:
        generators.append([(pt_x, pt_y), random_color()])

    #draw_point(img, pt_x, pt_y)

# Reordering generators:
print(generators)
generators.sort(key=lambda x: x[0])
print(generators)

def pt_star(point, generators):
    # find the nearest generator:
    d = min([ dist(point, i[0]) for i in generators ])
    return [point[0], point[1] + d]

for x in range(len(img)):
    for y in range(len(img[0])):
        # Find the color of [x,y] as the color of the nearest generator
        d = [ dist([x,y], i[0]) for i in generators]
        img[x][y] = generators[d.index(min(d))][1]

for pt in generators:
    draw_circle(img, pt[0][0], pt[0][1], 5, mcolors.to_rgb('black'))

plt.imshow(img)
plt.show()