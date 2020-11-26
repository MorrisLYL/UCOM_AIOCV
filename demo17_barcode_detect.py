import cv2
import os
import matplotlib.pyplot as plt

print(os.getcwd())
BARCODE = 'images/barcode_sample.jpg'
image = cv2.imread(BARCODE)
data, bounding_box, image = cv2.QRCodeDetector().detectAndDecode(image)
print(type(data))
print(type(bounding_box))
print(type(image))