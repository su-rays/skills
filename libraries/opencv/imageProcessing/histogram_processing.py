import cv2

# Read an image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg", 0)  # Grayscale

# Histogram equalization
equalized = cv2.equalizeHist(image)

# Display results
cv2.imshow('Equalized', equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()