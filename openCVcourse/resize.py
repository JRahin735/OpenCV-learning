import cv2 as cv


# resize function
def rescaleFrame(Frame, scale=0.75):
    dim = (int(Frame.shape[1] * scale), int(Frame.shape[0] * scale))
    return cv.resize(Frame, dim, interpolation=cv.INTER_AREA)


# reading in file
img = cv.imread('sample photos/blobs.jpg')
rescaled = rescaleFrame(img)
cv.imshow('blob resized', rescaled)
cv.imshow('blob original', img)


cv.waitKey(0)