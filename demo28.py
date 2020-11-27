import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = 'images/morph1.jpg'
image = cv2.imread(FILENAME)
plt.imshow(image)
# plt.show()
# 3,3, 5,5 , 77, 99

# ksize 越大 移除或擴大結果會越模糊
ksize = (9, 9)
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
plt.imshow(kernel1)
# plt.show()

morphedImage = image.copy()
for _ in range(20):
    # cv2.MORPH_OPEN >> 先移除再擴大
    # cv2.MORPH_CLOSE >> 先擴大在移除
    morphedImage = cv2.morphologyEx(morphedImage, cv2.MORPH_CLOSE, kernel1)

plt.figure(figsize=[15, 9])
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(morphedImage)
plt.show()