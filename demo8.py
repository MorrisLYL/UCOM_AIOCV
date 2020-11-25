import cv2
import matplotlib.pyplot as plt

IMAGE1 = 'images/bg.jpeg'
originalImage = cv2.imread(IMAGE1, -1)
plt.imshow(originalImage[:, :, ::-1])
plt.title("original image")
plt.show()

text1 = "hello opencv in python"
cv2.putText(originalImage, text1, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255),
            thickness=2, lineType=cv2.LINE_AA)
cv2.putText(originalImage, text1, (50, 250), cv2.FONT_ITALIC, 2, (0, 0, 255),
            thickness=2, lineType=cv2.LINE_AA)
plt.imshow(originalImage[:, :, ::-1])
plt.show()