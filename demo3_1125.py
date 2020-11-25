import cv2
import matplotlib
from matplotlib import pyplot as plt

path = 'images/number_zero.jpg'
matplotlib.rcParams['image.cmap'] = 'gray'
img = cv2.imread(path, 1)
print(type(img), img.shape)
# cv2.imshow("cv2", img)
plt.imshow(img)
plt.show()

# data type
print(img.dtype)
print(img[0, 0])

plt.figure(figsize=[14, 6])
img[0, 0] = (255, 0, 0)
img[1, 1] = (0, 255, 0)
img[2, 2] = (0, 0, 255)
# img 上列修正就是BGR的數值
plt.imshow(img[:,:,::-1])
plt.show()
cv2.imshow("cv2 change", img) # cv2 BGR

# pyplot RGB
plt.subplot(1, 3, 1)
cv2.imshow("first channel", image1[:, :, 0])
plt.title("first channel")
plt.imshow(image1[:, :, 0])
plt.subplot(1, 3, 2)
cv2.imshow("second channel", image1[:, :, 1])
plt.title("second channel")
plt.imshow(image1[:, :, 1])
plt.subplot(1, 3, 3)
cv2.imshow("third channel", image1[:, :, 2])
plt.title("third channel")
plt.imshow(image1[:, :, 2])
plt.show()