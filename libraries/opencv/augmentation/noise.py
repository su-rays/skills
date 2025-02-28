import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Add Gaussian noise
noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)

# Display
cv2.imshow("Original", image)
cv2.imshow("Noisy", noisy_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()