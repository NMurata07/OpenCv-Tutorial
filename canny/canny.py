import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def nothing(x):
    pass

img = cv2.imread(sys.argv[1], 0)
edge = cv2.Canny(img, 100, 100)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edge, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()