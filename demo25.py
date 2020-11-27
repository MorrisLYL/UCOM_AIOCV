import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = 'images/morph1.jpg'
image = cv2.imread(FILENAME)
plt.imshow(image)
plt.show()

ksize = (9, 9) # change this more big would let picture less white
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
plt.imshow(kernel1)
#plt.show()

# 先擴張再移除 會保留更多原圖的邊緣 達到去除白色的作用
morphedImage = cv2.dilate(image, kernel1)
morphedImage = cv2.erode(morphedImage, kernel1)
for _ in range(10):
    morphedImage = cv2.dilate(morphedImage, kernel1)
    morphedImage = cv2.erode(morphedImage, kernel1)
#morphedImage = cv2.erode(morphedImage, kernel1)

plt.figure(figsize=[15, 9])
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.imshow(morphedImage)
plt.show()