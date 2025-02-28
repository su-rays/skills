import cv2

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# convert color to gray
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# convert color to hsv
hsv_img  = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# convert color to rgb
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# convert color to lab
lab_img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# convert color to yuv
ycrcb_img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# convert color to hsl
hls_img = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

# convert color to xyz
xyz_img = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)


# display
cv2.imshow("rgb", rgb_img)
cv2.imshow('lab', lab_img)
cv2.imshow("yuv", ycrcb_img)
cv2.imshow("hsl", hls_img)
cv2.imshow("xyz", xyz_img)
cv2.imshow("gray", gray_img)
cv2.imshow("hsv", hsv_img)

# wait for key to press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()