import cv2

#read image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Gaussian blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# median blur
median_blur = cv2.medianBlur(image, 5)

# bilateral blur
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

# display
cv2.imshow("Gaussian blur", gaussian_blur)
cv2.imshow("median blur", median_blur)
cv2.imshow("bilateral blur", bilateral_blur)

# wait for key to press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()