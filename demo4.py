
import cv2
import matplotlib.pyplot as plt

IMAGE1 = 'images/transparency1.png'
image1 = cv2.imread(IMAGE1, -1)
image2 = cv2.imread(IMAGE1, 0)
image3 = cv2.imread(IMAGE1, 1)
print(f"read as -1, shape={image1.shape}")
print(f"read as 2, shape={image2.shape}")
print(f"read as 3, shape={image3.shape}")
cv2.imshow("read as -1", image1)
plt.imshow(image1)
plt.show()
cv2.imshow("read as 0", image2)
plt.imshow(image2)
plt.show()
cv2.imshow("read as 1", image3)
plt.imshow(image3)
plt.show()

image4 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
plt.title("correct with alpha channel(-1=keep)")
plt.imshow(image4)
plt.show()
print(f"image4 with dimension=={image4.shape}")
image5 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)
plt.title("correct without alpha(1, color)")
plt.imshow(image5)
plt.show()
print(f"image5 with dimension=={image5.shape}")


image6 = image1[:, :, :3]
# 最後3 表示BGR 0 1 2 三層我都要
image7 = image1[:, :, -1]
# 最後-1僅剩下透明層 最後一層
plt.figure(figsize=[12, 4])
plt.subplot(131)
plt.imshow(image6)
plt.subplot(132)
plt.imshow(image6[:, :, ::-1])
# -1 表示倒轉 BGR>>>RGB
plt.subplot(133)
plt.imshow(image7)
plt.show()