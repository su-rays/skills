import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# display the image
cv2.imshow("cat", image)

# wait for key press then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# write the image
cv2.imwrite("cat1.jpg", image)