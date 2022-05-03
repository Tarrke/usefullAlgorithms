# Description: This program cconverts an image to a pencil sketch

import cv2
from cv2 import pencilSketch

img_location = './drawingInPython/Pictures/'
img_name = 'spider-monkey.jpg'

img = cv2.imread(img_location+img_name)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_image = 255 - gray_image

blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred_image = 255- blurred_image

pencil_sketched_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow('Original Image', img)
cv2.imshow('Grayscaled Image', pencil_sketched_image)
cv2.waitKey(0)
