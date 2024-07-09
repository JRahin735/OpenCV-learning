import cv2 as cv


img = cv.imread('sample photos/data/aero3.jpg')

# gray-scaling
greyed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', greyed)

# blurred
blurred = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blurred)

# edge cascade
edge = cv.Canny(img, 125, 125)
cv.imshow('canny', edge)

# reducing the num of edges by blurring
edge2 = cv.Canny(blurred, 125, 125)
cv.imshow('canny2', edge2)

# Dilating the image
dilated = cv. dilate(edge, (7,7), iterations=3)
cv. imshow( 'Dilated', dilated)
# Eroding
eroded = cv. erode(edge, (7,7), iterations=3)
cv. imshow( 'Eroded', eroded)

cv.waitKey(0)