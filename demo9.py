import cv2

capture = cv2.VideoCapture(0)
while True:
    returnValue, frame = capture.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("IP CAM", frame_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    pass
capture.release()
