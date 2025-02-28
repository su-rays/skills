import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Define translation matrix
tx, ty = 50, 100  # Shift 50px right, 100px down
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Perform translation
translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Display
cv2.imshow("Original", image)
cv2.imshow("Translated", translated_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()