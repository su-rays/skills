import cv2
import numpy as np

# read image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# kernal
kernel = np.ones((5, 5), np.uint8)

# erosion 
eroded = cv2.erode(image, kernel, iterations=1)

# Dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# opening
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# closing
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# display
cv2.imshow("eorded image", eroded)
cv2.imshow("dilated image", dilated)
cv2.imshow("opened image", opened)
cv2.imshow("closed image", closed)

# wait and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()