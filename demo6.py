import cv2
import matplotlib.pyplot as plt

IMAGE1 = 'images/bg.jpeg'
originalImage = cv2.imread(IMAGE1, -1)
plt.imshow(originalImage[:, :, ::-1])
plt.title("original image")
plt.show()

cv2.circle(originalImage, (250, 250), 100, (255, 255, 0),
           thickness=10, lineType=cv2.LINE_AA)
cv2.circle(originalImage, (150, 150), 100, (255, 0, 255),
           thickness=-1, lineType=None)
plt.imshow(originalImage[:, :, ::-1])
plt.show()
