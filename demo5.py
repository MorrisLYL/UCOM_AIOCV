import cv2
import matplotlib.pyplot as plt

IMAGE1 = 'images/bg.jpeg'
originalImage = cv2.imread(IMAGE1, -1)
plt.imshow(originalImage[:, :, ::-1])
plt.title("original image")
plt.show()

for i in range(0, 20):
    cv2.line(originalImage, (200, 80 + 20 * i), (480, 80 + 10 * i),
             (255 - 10 * i, 0 + 10 * i, 0), thickness=3, lineType=cv2.LINE_AA)

plt.imshow(originalImage[:, :, ::-1])
plt.title("image draw line")
plt.show()
