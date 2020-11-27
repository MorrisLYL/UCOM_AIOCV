import cv2
from matplotlib import pyplot as plt
import time
import numpy as np

FILENAME = 'images/grayscale1.jpg'

sourceImage = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)

THRESHOLD_VALUE = 128
MAX_VALUE = 255
th, ret1 = cv2.threshold(sourceImage, THRESHOLD_VALUE, MAX_VALUE, cv2.THRESH_BINARY)
# auto change threshold mean 平均數  GAUSSIAN 高私函數
ret2 = cv2.adaptiveThreshold(sourceImage, MAX_VALUE, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 43, 9)
ret3 = cv2.adaptiveThreshold(sourceImage, MAX_VALUE, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 43, 9)
print(type(ret2), type(ret3))
print(ret2.shape, ret3.shape, ret1.shape)

titles = ['original',
          'global threshold=%d' % THRESHOLD_VALUE,
          'adaptive mean with blocksize=23, c=9',
          'adaptive gaussian with blocksize=23, c=9']
images = [sourceImage, ret1, ret2, ret3]
for i in range(len(images)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()