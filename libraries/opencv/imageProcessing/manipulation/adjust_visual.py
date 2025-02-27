import cv2
import numpy as np

# read the image
image = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")

# adjust brightness and contrast
alpha = 1.5 # contrast control
beta = 50 # brightness control
adjusted_img = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# adjust gemma
gamma = 1.5
lookup_table = np.array([((i/255.0)**gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
gamma_corrected_img = cv2.LUT(image, lookup_table)

# display
cv2.imshow("brightness and contrast", adjusted_img)
cv2.imshow("gamma", gamma_corrected_img)

# wait for key to press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()