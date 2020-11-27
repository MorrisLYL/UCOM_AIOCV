import cv2
import os
import matplotlib.pyplot as plt

import cv2
import os
from matplotlib import pyplot

print(os.getcwd())
BARCODE_FILE1 = 'images/barcode_sample.jpg'
originalImage = cv2.imread(BARCODE_FILE1)
data, bbox, extractedImage = cv2.QRCodeDetector().detectAndDecode(originalImage)
print(type(data))
print(type(bbox), bbox.shape)
print(type(extractedImage))
# p1 p2 p3 p4 from bounding box array
print(f"bar code content={data}, bbox={bbox}")
cv2.imshow("original image", originalImage)
cv2.imshow("image extract from cv2", extractedImage)

OUTPUT_FILE = 'images/barcode_annotated.jpg'

def drawBBox(originalImage, bbox, barcodeData):
    COLOR1 = (128, 128, 0)
    p1 = (bbox[0][0][0], bbox[0][0][1])
    p2 = (bbox[0][1][0], bbox[0][1][1])
    p3 = (bbox[0][2][0], bbox[0][2][1])
    p4 = (bbox[0][3][0], bbox[0][3][1])
    cv2.line(originalImage, p1, p2, COLOR1, 2)
    cv2.line(originalImage, p2, p3, COLOR1, 2)
    cv2.line(originalImage, p3, p4, COLOR1, 2)
    cv2.line(originalImage, p4, p1, COLOR1, 2)
    cv2.imwrite(OUTPUT_FILE, originalImage)
    pyplot.imshow(originalImage)
    pyplot.title(f"barcode:{barcodeData} with bounding box")
    pyplot.show()


if data != None:
    drawBBox(originalImage, bbox, data)
else:
    print("QR code not Detected")