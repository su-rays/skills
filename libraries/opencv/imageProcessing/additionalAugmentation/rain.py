import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Create rain effect
h, w = image.shape[:2]
rain = np.zeros((h, w, 3), dtype=np.uint8)
num_drops = 1000
for _ in range(num_drops):
    x, y = np.random.randint(0, w), np.random.randint(0, h)
    length = np.random.randint(10, 30)
    cv2.line(rain, (x, y), (x, y + length), (255, 255, 255), 1)

# Blend rain with image
rain_strength = np.random.uniform(0.1, 0.3)
rainy_image = cv2.addWeighted(image, 1 - rain_strength, rain, rain_strength, 0)

# Display
cv2.imshow("Original", image)
cv2.imshow("Random Rain", rainy_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()