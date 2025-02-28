import cv2

# Read an image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Gaussian pyramid
lower_resolution = cv2.pyrDown(image)
higher_resolution = cv2.pyrUp(lower_resolution)

# Laplacian pyramid
laplacian = cv2.subtract(image, higher_resolution)

# Display results
cv2.imshow('Lower Resolution', lower_resolution)
cv2.imshow('Higher Resolution', higher_resolution)
cv2.imshow('Laplacian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()