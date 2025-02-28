import cv2
import numpy as np

# Read images
image1 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")
image2 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/dog.jpeg")
image3 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/bird.jpeg")
image4 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/fish.jpeg")

# Resize images to the same size
size = (200, 200)
image1 = cv2.resize(image1, size)
image2 = cv2.resize(image2, size)
image3 = cv2.resize(image3, size)
image4 = cv2.resize(image4, size)

# Create mosaic
mosaic = np.vstack((np.hstack((image1, image2)), np.hstack((image3, image4))))

# Display
cv2.imshow("Mosaic", mosaic)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()