import cv2
import matplotlib.pyplot as plt
import time

path = 'images/grayscale1.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# plt.imshow(img)
# plt.show()

THRESHOLD_VALUE = 50
maxValue = 255


def thresholdUsingLoop(image, threshold, v_max): # 14.81
    dst = image.copy()
    print(image.shape[:2])
    height, width = image.shape[:2]
    for i in range(height):
        for j in range(width):
            if img[i, j] > threshold:
                dst[i, j] = v_max
            else:
                dst[i, j] = 0
    return dst

plt.imshow(img)
startTime = time.time()
binaryImage = thresholdUsingLoop(img, THRESHOLD_VALUE, maxValue)
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
