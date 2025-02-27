import cv2

# Read an image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg", 0)  # Grayscale

# Binary thresholding
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Adaptive thresholding
adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Otsu's thresholding
_, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display results
cv2.imshow('Binary', binary)
cv2.imshow('Adaptive', adaptive)
cv2.imshow('Otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()