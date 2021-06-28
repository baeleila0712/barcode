from pyzbar import pyzbar
import cv2
import numpy as np

img1 = cv2.imread('123.jpg', 1)
cv2.imshow('image1', img1)

r = pyzbar.decode(img1)
print(r)
for i, d in enumerate(r):
	print('No.', i+1, "bar", d.type, ', content', d.data.decode('UTF-8'))


cv2.waitKey(0)
cv2.destroyAllWindows()