import cv2 as cv
import numpy as np


# Kinda stupid to follow along :/


blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('drew on', blank)

cv.waitKey(0)