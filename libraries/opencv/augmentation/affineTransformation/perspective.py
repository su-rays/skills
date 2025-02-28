import cv2
import numpy as np

# read image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# perspective transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)
perspective_transformed = cv2.warpPerspective(image, perspective_matrix, (300, 300))

# display
cv2.imshow("perspective", perspective_transformed)

# wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()