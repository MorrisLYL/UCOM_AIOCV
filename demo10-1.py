import cv2
import matplotlib.pyplot as plt
import math
from PIL import ImageFont, ImageDraw, Image
import numpy as np

IMAGE1 = 'images/bg.jpeg'
originalImage = cv2.imread(IMAGE1, -1)
imageCopy = originalImage.copy()


# center = (0, 0)
# bbox = (0, 0)


def drawCircle(action, x, y, flags, userdata):
    global center
    if action == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        print("left bottom down, at({}.{})".format(x, y))
        cv2.circle(originalImage, center, 1, (255, 255, 0), 6, cv2.LINE_AA)
    elif action == cv2.EVENT_LBUTTONUP:
        bbox = (x, y)
        radius = math.sqrt(math.pow(center[0] - bbox[0], 2) +
                           math.pow(center[1] - bbox[1], 2))
        cv2.circle(originalImage, center, int(radius), (0, 255, 255), 2, cv2.LINE_AA)
        print("left bottom release up, at({}.{})".format(x, y))


WINDOW_NAME = "main window"
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, drawCircle)
FONT_PATH = 'fonts/NotoSerifCJK-Regular.ttc'
# 字體大小
font = ImageFont.truetype(FONT_PATH, 36)

k = 0
while k != 27:
    cv2.imshow(WINDOW_NAME, originalImage)
    # 圖片讀取成PIL格式
    img_pil = Image.fromarray(originalImage)
    draw = ImageDraw.Draw(img_pil)
    draw.text((10, 200), "按下左鍵left click, and drag", font=font, fill=(255, 255, 0, 255))
    # pil 讀取圖片和cv2 格式不同 需轉換成array 才能在呈現
    originalImage = np.array(img_pil)
    # cv2.putText(originalImage, "按下左鍵left click, and drag", (50, 50),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    k = cv2.waitKey(20)
    if k == ord('c'):
        originalImage = imageCopy.copy()
cv2.destroyAllWindows()