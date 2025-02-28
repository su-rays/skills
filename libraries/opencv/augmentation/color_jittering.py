import cv2
import numpy as np

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Adjust brightness
brightness_factor = 1.5  # Increase brightness by 50%
brightened_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

# Adjust contrast
contrast_factor = 1.5  # Increase contrast by 50%
contrasted_image = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=0)

# adjust gemma
gamma = 1.5
lookup_table = np.array([((i/255.0)**gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
gamma_corrected_img = cv2.LUT(image, lookup_table)

# display
cv2.imshow("bright", brightened_image)
cv2.imshow("contrast", contrasted_image)
cv2.imshow("gamma", gamma_corrected_img)

# wait for key to press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()