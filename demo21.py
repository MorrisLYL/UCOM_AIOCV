import cv2
import matplotlib.pyplot as plt
import time
import numpy as np

path = 'images/grayscale1.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# plt.imshow(img)
# plt.show()

THRESHOLD_VALUE = 50
maxValue = 255


# def thresholdUsingLoop(image, threshold, v_max):  # 0.02
#     dst = np.zeros_like(image)
#     print(type(image), type(dst))
#     print(image.shape, dst.shape)
#     maxPixels = image > threshold
#     zeroPixels = image < threshold
#     dst[maxPixels] = v_max
#     dst[zeroPixels] = 0
#     return dst


plt.imshow(img)
startTime = time.time()
# %timeit cv2.threshold(img, THRESHOLD_VALUE, maxValue, cv2.THRESH_BINARY) 可至ipython test waste time
threshold_return, binaryImage = cv2.threshold(img, THRESHOLD_VALUE, maxValue, cv2.THRESH_BINARY)  #0.003
# binaryImage = thresholdUsingLoop(img, THRESHOLD_VALUE, maxValue)
endTime = time.time()
print(f"it took {endTime - startTime} to do threshold")
plt.show()
plt.subplot(121)
plt.title("original image")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(122)
plt.title("binary image")
plt.imshow(binaryImage, cmap='gray', vmin=0, vmax=255)
plt.show()
