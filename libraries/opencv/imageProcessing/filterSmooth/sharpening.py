import cv2
import numpy as np

# read image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# sharpening kernal
kernal = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_img = cv2.filter2D(image, -1, kernal)

# diaplay
cv2.imshow("sharpened", sharpened_img)

# wait for key to be pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()