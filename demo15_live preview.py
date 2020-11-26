import cv2
import torchvision.transforms as transforms
import torchvision
import torch
import PIL

MODEL_WEIGHT = 'model/weight_only'
cap = cv2.VideoCapture(0)

device = torch.device('cpu')
model1 = torchvision.models.resnet18()
model1 = model1.to(device)
model1.fc = torch.nn.Linear(512, 2)
model1.load_state_dict(torch.load(MODEL_WEIGHT))
TRANSFORMS = transforms.Compose([
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


def verify(f):
    global status
    image = f.to(device)
    image = torch.reshape(image, [1, 3, 224, 224])
    output = model1(image)
    if output.argmax(1) == 1:
        status = 'down'
        print("down")
    else:
        status = 'up'
        print("up")


status = '---'
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(gray, 'gesture=%s' % status, (50, 50), cv2.FONT_ITALIC, 2, (0, 0, 0), thickness=1)
    cv2.imshow("IP CAM", gray)
    inputKey = cv2.waitKey(1) & 0xFF
    if inputKey == ord('q'):
        break
    elif inputKey == ord('t'):
        print("call pytorch")
        frame = PIL.Image.fromarray(frame)
        frame = TRANSFORMS(frame)
        verify(frame)

cap.release()
cv2.destroyAllWindows()
