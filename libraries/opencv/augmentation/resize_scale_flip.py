import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# resize the image
resized_img = cv2.resize(image, (640, 480))

# Zoom in/out
scale_factor = 1.5  # Scale by 1.5x
scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

# flip the image
flipped_img = cv2.flip(image, 0)  # 1 for horizontal, 0 for vertical

# display
cv2.imshow("resized", resized_img)
cv2.imshow("zoom in/out", scaled_image)
cv2.imshow("flipped", flipped_img)

# wait for key to press the close the window
cv2.waitKey(0)
cv2.destroyAllWindows()