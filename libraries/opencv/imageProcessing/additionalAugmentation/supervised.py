import cv2
import numpy as np

# Read image and bounding box
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")
x, y, w, h = 100, 100, 200, 200  # Example bounding box

# Flip image and bounding box
flipped_image = cv2.flip(image, 1)
flipped_x = image.shape[1] - x - w  # Adjust bounding box for horizontal flip

# Draw bounding box
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.rectangle(flipped_image, (flipped_x, y), (flipped_x + w, y + h), (0, 255, 0), 2)

# Display
cv2.imshow("Original", image)
cv2.imshow("Flipped with Bounding Box", flipped_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()