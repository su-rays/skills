import cv2
import numpy as np

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# Adjust brightness and contrast for simple tasks
contrast_factor = 1.5  # Increase contrast by 50%
brightness_factor = 50 # Increase brightness by 50%
brightened_image = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=brightness_factor)

# adjust gemma for more natural process 
gamma = 9.0
lookup_table = np.array([((i/255)**gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
gamma_corrected_img = cv2.LUT(image, lookup_table)

# display
cv2.imshow("original", image)
cv2.imshow("bright", brightened_image)
cv2.imshow("gamma", gamma_corrected_img)

# wait for key to press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()