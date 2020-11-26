import cv2

# for first camera, select 0
capture = cv2.VideoCapture(0)
p_counter = 0
n_counter = 0
POSITIVE_NAME = 'image/positive/%d.jpg'
NEGATIVE_NAME = 'image/negative/%d.jpg'

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    inputKey = cv2.waitKey(1)
    # show is gray but catch picture is color
    if inputKey & 0xFF == ord('q'):
        break
    elif inputKey & 0xFF == ord('p'):
        filename = POSITIVE_NAME % p_counter
        cv2.imwrite(filename, frame)
        print(f"positive file {filename} saved")
        p_counter += 1
    elif inputKey & 0xFF == ord('n'):
        filename = NEGATIVE_NAME % n_counter
        cv2.imwrite(filename, frame)
        print(f"negative file {filename} saved")
        n_counter += 1
capture.release()
cv2.destroyAllWindows()