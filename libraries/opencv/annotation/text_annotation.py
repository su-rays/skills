import cv2
import numpy as np

# Create a blank image (white background)
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Add text to the image (text, position, font, scale, color, thickness)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "Hello, OpenCV!", (50, 250), font, 1, (0, 0, 0), 2)

# Display the image
cv2.imshow("Text Annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()