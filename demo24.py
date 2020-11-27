import cv2
import matplotlib.pyplot as plt

kernels = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]

plt.figure(figsize=[15, 15])
for i, k in zip([1, 2, 3], kernels):
    # k 後面放的 ksize 使用奇數
    a1 = cv2.getStructuringElement(k, (15, 15))
    plt.subplot(1, 3, i)
    plt.imshow(a1, 'gray')
    print(a1)

plt.show()
