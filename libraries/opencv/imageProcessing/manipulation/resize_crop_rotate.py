import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# resize the image
resized_img = cv2.resize(image, (640, 480))

# crop the image
cropped_img = image[50:200, 100:300]

# rotate the image
h, w = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(image, rotation_matrix, (w, h))

# flip the image
flipped_img = cv2.flip(image, 0)  # 1 for horizontal, 0 for vertical

# display
cv2.imshow("resized", resized_img)
cv2.imshow("cropped", cropped_img)
cv2.imshow("rotated", rotated_img)
cv2.imshow("flipped", flipped_img)

# wait for key to press the close the window
cv2.waitKey(0)
cv2.destroyAllWindows()