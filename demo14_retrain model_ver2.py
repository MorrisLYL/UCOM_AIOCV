import torchvision.transforms as transforms
from demo13_dataset import ImageClassificationDataset
import torchvision
import torch
import torch.nn.functional as F

TASK = 'image'
CATEGORIES = ['positive', 'negative']
DATASETS = ['image']
TRANSFORMS = transforms.Compose([
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

datasets = {}
for name in DATASETS:
    datasets[name] = ImageClassificationDataset(name, CATEGORIES, TRANSFORMS)
dataset = datasets[DATASETS[0]]
print(f"{TASK} task with {CATEGORIES} categories defined")
dataset._refresh()
train_loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=True)
device = torch.device('cpu')
model = torchvision.models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(512, len(dataset.categories))
model = model.to(device)
model.train()
print(model)
epochs = 10
optimizer = torch.optim.Adam(model.parameters())
while epochs > 0:
    i = 0
    sum_loss = 0.0
    error_count = 0.0
    for img, lbl in iter(train_loader):
        img = img.to(device)
        lbl = lbl.to(device)
        optimizer.zero_grad()
        outputs = model(img)
        loss = F.cross_entropy(outputs, lbl)
        print(f"loss={loss}")
        loss.backward()
        optimizer.step()
        error_count += len(torch.nonzero(outputs.argmax(1) - lbl, as_tuple=False).flatten())
        count = len(lbl.flatten())
        i += count
        sum_loss += float(loss)
    print("[{}],loss={},accuracy={}".format(epochs, sum_loss, 1.0 - error_count / i))
    epochs = epochs - 1
MODEL_WEIGHT = 'model/weight_only'
WHOLE_MODEL = 'model/model_and_weight'
torch.save(model.state_dict(), MODEL_WEIGHT)
torch.save(model, WHOLE_MODEL)

val_dataset = ImageClassificationDataset("val_image", CATEGORIES, TRANSFORMS)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=1)

i = 0
error_count = 0

for image, label in iter(val_loader):
    image = image.to(device)
    label = label.to(device)
    output = model(image)
    print(f"label={label}, guess={output.argmax(1)}")
    error_count += len(torch.nonzero(output.argmax(1) - label).flatten())
    count = len(label.flatten())
    i += count
print("error_count=", error_count)
print("tota=", i)