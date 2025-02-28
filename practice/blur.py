import cv2

image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

median_blur_1 = cv2.bilateralFilter(image, 99, 75, 75)
median_blur_99 = cv2.bilateralFilter(image, 99, 755, 755)

cv2.imshow("gaussian 1", median_blur_1)
cv2.imshow("gaussian 9", median_blur_99)

cv2.waitKey(0)
cv2.destroyAllWindows()