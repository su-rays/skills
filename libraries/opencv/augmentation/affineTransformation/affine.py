import cv2
import numpy as np

# read image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# affine transformation
rows, cols = image.shape[:2]
pts1 = np.float32([[50, 50], [50, 200], [200, 50]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
affine_matrix = cv2.getAffineTransform(pts1, pts2)
affine_transformed =  cv2.warpAffine(image, affine_matrix, (rows, cols))

# display
cv2.imshow("affine", affine_transformed)

# wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()