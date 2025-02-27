import cv2

# Read two images
image1 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")
image2 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/dog.jpeg")

# Resize images to the same size
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Alpha blending
alpha = 0.5
blended = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)

# Display results
cv2.imshow('Blended', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
