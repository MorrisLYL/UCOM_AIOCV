import cv2

capture = cv2.VideoCapture(0)
counter = 0
IMAGE_NAME = 'image/%d.jpg'

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Webcam", gray)
    inputKey = cv2.waitKey(1)
    if inputKey & 0xFF == ord('q'):
        break
    elif inputKey & 0xFF == ord('s'):
        filename = IMAGE_NAME % counter
        cv2.imwrite(filename, gray)
        print(f'file {filename} saved')
        counter += 1
capture.release()
cv2.destroyAllWindows()
