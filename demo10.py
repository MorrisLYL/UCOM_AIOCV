import cv2
import math

path = 'images/bg.jpeg'
image = cv2.imread(path, -1)
# 複製保留原圖
copeimg = image.copy()
# center = (0, 0)
# bbox = (0, 0)


def drawCircle(action, x, y, flags, userdata):
    global center
    if action == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        print("left button down at({},{})".format(x, y))
        cv2.circle(image, center, 1, (255, 255, 0), 6, cv2.LINE_AA)
    elif action == cv2.EVENT_LBUTTONUP:
        bbox = (x, y)
        radius = math.sqrt(math.pow(center[0] - bbox[0], 2) +
                           math.pow(center[1] - bbox[1], 2))
        cv2.circle(image, center, int(radius), (0, 255, 255), 2, cv2.LINE_AA)
        print("Left button up at({},{})".format(x, y))


main = "main"
cv2.namedWindow(main)
cv2.setMouseCallback(main, drawCircle)

k = 0
while k != 27:  # 27=esc鍵
    cv2.imshow(main, image)
    cv2.putText(image, "left click, and drag", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    if k == ord('c'):
        image = copeimg.copy()
    k = cv2.waitKey(20)
cv2.destroyAllWindows()
