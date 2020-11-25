import cv2
import matplotlib
import matplotlib.pyplot as plt

path = 'images/bg.jpeg'
matplotlib.rcParams['image.cmap'] = 'gray'
img = cv2.imread(path)
plt.imshow(img)
plt.show()
print(f'img default dim={img.shape}')


img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.title("Change to RGB")
plt.imshow(img2)
plt.show()

img3 = img[:, :, ::-1]
plt.title("Same dif coding")
plt.imshow(img3)
plt.show()

plt.figure(figsize=[20, 9])
plt.subplot(131)
plt.title("b channel")
plt.imshow(img[:,:,0])
plt.subplot(132)
plt.title("g channel")
plt.imshow(img[:,:,1])
plt.subplot(133)
plt.title("r channel")
plt.imshow(img[:,:,2])
plt.show()


b, g, r = cv2.split(img)
# result = cv2.split(img)
plt.figure(figsize=[20, 9])
plt.subplot(131)
plt.title("b channel")
plt.imshow(b)
# plt.imshow(result[0])
plt.subplot(132)
plt.title("g channel")
plt.imshow(g)
# plt.imshow(result[1])
plt.subplot(133)
plt.title("r channel")
plt.imshow(r)
# plt.imshow(result[2])
plt.show()