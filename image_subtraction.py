import cv2
import numpy as np

image1 = cv2.imread("star.jpg")
image2 = cv2.imread("dot.jpg")

sub = cv2.subtract(image1, image2)

cv2.imshow("Subtraction", sub)
cv2.waitKey(0)
