import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# rotate the image
h, w = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(image, rotation_matrix, (w, h))

# display
cv2.imshow("rotated", rotated_img)

# wait for key to press the close the window
cv2.waitKey(0)
cv2.destroyAllWindows()