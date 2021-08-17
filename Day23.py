import cv2
#to read the image
img = cv2.imread("sen.jpg")
# get dimensions of image
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ', dimensions)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)

#to show the image
cv2.imshow("sen", img)
cv2.waitKey(0)