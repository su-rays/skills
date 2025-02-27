import cv2
import numpy as np
from scipy.ndimage import map_coordinates, gaussian_filter

# Read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Define elastic deformation parameters
alpha = 1000  # Intensity of deformation
sigma = 8     # Smoothness of deformation

# Perform elastic deformation
random_state = np.random.RandomState(None)
shape = image.shape[:2]
dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha
dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha
x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
indices = np.reshape(y + dy, (-1, 1)), np.reshape(x + dx, (-1, 1))

# Correct the shape of the indices array
indices = np.array([y + dy, x + dx]).reshape(2, -1)

# Apply the deformation to each channel separately
distorted_image = np.zeros_like(image)
for i in range(image.shape[2]):
    distorted_image[..., i] = map_coordinates(image[..., i], indices, order=1, mode='reflect').reshape(shape)

# Display
cv2.imshow("Original", image)
cv2.imshow("Elastic Deformation", distorted_image)

# Wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()