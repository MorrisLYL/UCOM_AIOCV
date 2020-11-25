import cv2
import matplotlib.pyplot as plt
import matplotlib

path = 'images/number_zero.jpg'
img1 = cv2.imread(path, 0)
print(img1)
print(type(img1))
print(img1.dtype)
print(img1[0][0], type(img1[0][0]))
print(img1.shape)


# img1[0][0]=255
# img1[0][1]=255
# img1[1][0]=255
# img1[1][1]=255
# print("handwrite", img1)

for i in range(2):
    for j in range(2):
        img1[i][j] = 255
print("for run", img1)

img1[0:6, 0:4] = 128
plt.plot(img1)
cv2.imshow("cv2", img1)
plt.imshow(img1)
plt.show()
# # --------------------

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
plt.imshow(img1)
plt.colorbar()
plt.show()