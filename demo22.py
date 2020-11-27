import cv2
from matplotlib import pyplot as plt
import time
import numpy as np

PATH = 'images/grayscale1.jpg'

sourceImg = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

THRESHOLD_VALUE = 200
MAX_VALUE = 255

THRESHOLDS = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]
resultImages = []
for i, t in enumerate(THRESHOLDS):
    print(f"[{i}],threshold={t}")
    _, resultImg = cv2.threshold(sourceImg, THRESHOLD_VALUE, MAX_VALUE, t)
    resultImages.append(resultImg)
    # resultImages += [resultImg]

print(len(resultImages))
# subplot 2*3 直2橫3
plt.subplot(2, 3, 1)
plt.title('original image')
plt.imshow(sourceImg, cmap='gray', vmin=0, vmax=255)
plt.subplot(2, 3, 2)
plt.title('binary threshold image')
plt.imshow(resultImages[0], cmap='gray', vmin=0, vmax=255)
plt.subplot(2, 3, 3)
plt.title('binary threshold inverse image')
plt.imshow(resultImages[1], cmap='gray', vmin=0, vmax=255)
plt.subplot(2, 3, 4)
plt.title('binary threshold truncate')
plt.imshow(resultImages[2], cmap='gray', vmin=0, vmax=255)
plt.subplot(2, 3, 5)
plt.title('binary threshold zero')
plt.imshow(resultImages[3], cmap='gray', vmin=0, vmax=255)
plt.subplot(2, 3, 6)
plt.title('binary threshold zero inverse')
plt.imshow(resultImages[4], cmap='gray', vmin=0, vmax=255)


plt.show()
