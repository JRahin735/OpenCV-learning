import cv2 as cv

img = cv.imread('sample photos/blobs.jpg')
cv.imshow('blob', img)

cv.waitKey(0)