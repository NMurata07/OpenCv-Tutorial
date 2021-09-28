import cv2
import numpy as np
import sys

def nothing(x):
    pass

img = cv2.imread(sys.argv[1], 0)
cv2.namedWindow('edge')
cv2.createTrackbar('minVal', 'edge', 10, 100, nothing)
cv2.createTrackbar('maxVal', 'edge', 110, 400, nothing)

while(1):
    minVal = cv2.getTrackbarPos('minVal', 'edge')    
    maxVal = cv2.getTrackbarPos('maxVal', 'edge')
    edge = cv2.Canny(img, minVal, maxVal)
    cv2.imshow('edge', edge)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows