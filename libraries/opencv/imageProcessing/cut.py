import cv2
import numpy as np

# Read the image
image1 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Define erase region
x, y, w, h = 50, 50, 100, 100  # Erase a 100x100 region starting at (50, 50)

# Perform random erasing
image1[y:y+h, x:x+w] = np.random.randint(0, 255, (h, w, 3)) # 0 for cutout

# Display
cv2.imshow("Image", image1)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()