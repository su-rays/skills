import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Create snow effect
h, w = image.shape[:2]
snow = np.zeros((h, w, 3), dtype=np.uint8)
num_flakes = 1000
for _ in range(num_flakes):
    x, y = np.random.randint(0, w), np.random.randint(0, h)
    cv2.circle(snow, (x, y), np.random.randint(1, 3), (255, 255, 255), -1)

# Blend snow with image
snow_strength = np.random.uniform(0.1, 0.3)
snowy_image = cv2.addWeighted(image, 1 - snow_strength, snow, snow_strength, 0)

# Display
cv2.imshow("Original", image)
cv2.imshow("Random Snow", snowy_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()