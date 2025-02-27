import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Create a random shadow mask
h, w = image.shape[:2]
shadow_mask = np.zeros((h, w), dtype=np.uint8)
x1, y1 = np.random.randint(0, w), np.random.randint(0, h)
x2, y2 = np.random.randint(0, w), np.random.randint(0, h)
cv2.rectangle(shadow_mask, (x1, y1), (x2, y2), 255, -1)

# Apply shadow
shadow_strength = np.random.uniform(0.3, 0.7)
shadowed_image = cv2.addWeighted(image, 1 - shadow_strength, cv2.cvtColor(shadow_mask, cv2.COLOR_GRAY2BGR), shadow_strength, 0)

# Display
cv2.imshow("Original", image)
cv2.imshow("Random Shadows", shadowed_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()