import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Create fog effect
h, w = image.shape[:2]
fog = np.random.normal(128, 50, (h, w, 3)).astype(np.uint8)
fog_strength = np.random.uniform(0.3, 0.7)
foggy_image = cv2.addWeighted(image, 1 - fog_strength, fog, fog_strength, 0)

# Display
cv2.imshow("Original", image)
cv2.imshow("Random Fog", foggy_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()