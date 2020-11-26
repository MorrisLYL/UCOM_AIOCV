import torchvision.transforms as transforms
from demo13_dataset import ImageClassificationDataset
import torchvision
import torch
import torch.nn.functional as F

TASK = 'image'
CATEGORIES = ['positive', 'negative']
DATASETS = ['image']
TRANSFORMS = transforms.Compose([
    # image preprocess
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    # transforms.Resize((244, 244)),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

datasets = {}
for name in DATASETS:
    datasets[name] = ImageClassificationDataset(name, CATEGORIES, TRANSFORMS)
datasets = datasets[DATASETS[0]]
print(f"{TASK} task with {CATEGORIES} categories defined")
# 避免有人繼續放入資料
datasets._refresh()

train_loader = torch.utils.data.DataLoader(datasets, batch_size=1, shuffle=True)
device = torch.device('cpu')
# device = torch.device('cuda')
model = torchvision.models.resnet18(pretrained=True)
# 同一層有512node
model.fc = torch.nn.Linear(512, len(datasets.categories))
model = model.to(device)
model.train()
print(model)

epochs = 15
optimizer = torch.optim.Adam(model.parameters())
while epochs > 0:
    i = 0
    sum_loss = 0.0
    error_count = 0.0
    for images, labels in iter(train_loader):
        images = images.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = F.cross_entropy(outputs, labels)
        loss.backward()
        optimizer.step()
        error_count += len(torch.nonzero(outputs.argmax(1) - labels, as_tuple=False).flatten())
        count = len(labels.flatten())
        i += count
        sum_loss += float(loss)
    print("[{}],loss={},accuracy={}".format(epochs, sum_loss / i, 1.0 - error_count / i))
    epochs = epochs - 1

# MODEL_WEIGHT = 'model/weight_only'
MODEL_WEIGHT = 'model/weight_only_color'
# WHOLE_MODEL = 'model/model_and_weight'
WHOLE_MODEL = 'model/model_and_weight_color'
torch.save(model.state_dict(), MODEL_WEIGHT)
# better save
torch.save(model, WHOLE_MODEL)
