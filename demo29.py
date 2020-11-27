import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = 'images/mickey.jpg'
image = cv2.imread(FILENAME)
plt.imshow(image)

# ksize >> kernel
ksize = (5, 5)
k1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
plt.imshow(k1)

morphedImage = image.copy()
# erode while less black more
morph1 = cv2.morphologyEx(morphedImage, cv2.MORPH_ERODE, k1)
# dilate while more black less
morph2 = cv2.morphologyEx(morphedImage, cv2.MORPH_DILATE, k1)
# gradient
morph3 = cv2.morphologyEx(morphedImage, cv2.MORPH_GRADIENT, k1)

plt.figure(figsize=[12,6])
plt.subplot(141)
plt.title("original")
plt.imshow(image)
plt.subplot(142)
plt.title("erode")
plt.imshow(morph1)
plt.subplot(143)
plt.title("dilate")
plt.imshow(morph2)
plt.subplot(144)
plt.title("gradient")
plt.imshow(morph3)
plt.show()