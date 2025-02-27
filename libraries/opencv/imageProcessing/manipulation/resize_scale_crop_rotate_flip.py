import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# resize the image
resized_img = cv2.resize(image, (640, 480))

# crop the image
x, y, w, h = 100, 100, 200, 200  # Crop a 200x200 region starting at (100, 100)
cropped_img = image[y:y+h, x:x+w]

# Zoom in/out
scale_factor = 1.5  # Scale by 1.5x
scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

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