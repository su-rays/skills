import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# convert color to gray
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# convert color to HSV
hsv_img  = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# display
cv2.imshow("gray", gray_img)
cv2.imshow("hsv", hsv_img)

# wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()