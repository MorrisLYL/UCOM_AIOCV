import torch
import torchvision
from torchvision import transforms
from demo13_dataset import ImageClassificationDataset

# normal setting
TRANSFORMS = transforms.Compose([
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

MODEL_WEIGHT = 'model/weight_only'
WHOLE_MODEL = 'model/model_and_weight'

device = torch.device('cpu')
model1 = torchvision.models.resnet18()
model1 = model1.to(device)
model1.fc = torch.nn.Linear(512, 2)
model1.load_state_dict(torch.load(MODEL_WEIGHT))

model2 = torch.load(WHOLE_MODEL)
print("---")


def compare_models(m1, m2):
    models_differ = 0
    for key_item1, key_item2 in zip(m1.state_dict().items(), m2.state_dict().items()):
        if torch.equal(key_item1[1], key_item2[1]):
            pass
        else:
            models_differ += 1
            if key_item1[0] == key_item2[0]:
                print("mismatch found at:{}".format(key_item1[0]))
            else:
                raise Exception
    if models_differ == 0:
        print("model match perfectly")


compare_models(model1, model2)
FILE1 = 'model/model1.txt'
FILE2 = 'model/model2.txt'
with open(FILE1, 'w') as file1:
    file1.write(str(model1))
with open(FILE2, 'w') as file2:
    file2.write(str(model2))
