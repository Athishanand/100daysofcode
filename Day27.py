import cv2
import numpy as np

FILE_NAME = 'cow.jpg'
try:
    # Read image from disk.
    img = cv2.imread("cow.jpg")

    # to scale
    (height, width) = img.shape[:2]

    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

    # to rotate
    (rows, cols) = img.shape[:2]

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))

    # Edge detection
    edges = cv2.Canny(img, 100, 200)


    cv2.imwrite('result.jpg', res)

except IOError:
    print ('Error while reading files !!!')

