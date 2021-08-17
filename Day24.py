import numpy as np
import cv2
my_img = np.zeros((400, 400, 3), dtype = "uint8")

# creating a rectangle
cv2.rectangle(my_img, (30, 30), (300, 200), (0, 20, 200), 10)

# creating circle
cv2.circle(my_img, (200, 200), 80, (0, 20, 200), 10)

# allows us to see image
cv2.imshow('Window', my_img)
cv2.waitKey(0)

