import cv2
import numpy as np

# Create a blank image (white background)
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw a marker (center coordinates, marker type, size, color, thickness)
cv2.drawMarker(image, (250, 250), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)

# Display the image
cv2.imshow("Marker", image)
cv2.waitKey(0)
cv2.destroyAllWindows()