import cv2
import matplotlib.pyplot as plt

IMAGE1 = 'images/bg.jpeg'
originalImage = cv2.imread(IMAGE1, -1)
plt.imshow(originalImage[:, :, ::-1])
plt.title("original image")
plt.show()


# 400 > 300 > 200 x軸漸漸向左 中心座標漸漸往左
cv2.ellipse(originalImage, (400, 125), (200, 80), 0, 0, 360, (255, 0, 0), thickness=3,
            lineType=cv2.LINE_AA)
cv2.ellipse(originalImage, (300, 125), (200, 80), 45, 0, 360, (0, 255, 0), thickness=5,
            lineType=cv2.LINE_AA)
cv2.ellipse(originalImage, (200, 125), (200, 80), 90, 0, 360, (0, 0, 255), thickness=7,
            lineType=cv2.LINE_AA)
plt.imshow(originalImage[:, :, ::-1])
plt.title("annotated image")
plt.show()


cv2.ellipse(originalImage, (400, 125), (200, 80), 0, 0, 360, (255, 255, 255), thickness=3,
            lineType=cv2.LINE_AA)
cv2.ellipse(originalImage, (300, 125), (200, 120), 45, 0, 360, (255, 255, 255), thickness=5,
            lineType=cv2.LINE_AA)
cv2.ellipse(originalImage, (200, 125), (200, 150), 90, 0, 360, (255, 255, 255), thickness=7,
            lineType=cv2.LINE_AA)
plt.imshow(originalImage[:, :, ::-1])
plt.title("axes image")
plt.show()





# (200,80) axes  0,0,90 角度,起始角度,結束角度
cv2.ellipse(originalImage, (700, 325), (200, 80), 0, 0, 90, (0, 0, 255), thickness=5,
            lineType=cv2.LINE_AA)
cv2.ellipse(originalImage, (700, 325), (80, 200), 0, 180, 270, (0, 255, 255), thickness=5,
            lineType=cv2.LINE_AA)
cv2.ellipse(originalImage, (700, 325), (140, 140), 0, 270, 360, (255, 255, 0), thickness=-1,
            lineType=cv2.LINE_AA)
plt.imshow(originalImage[:, :, ::-1])
plt.title("angle image")
plt.show()