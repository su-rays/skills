import cv2
import numpy as np

# Create a blank image (white background)
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw a line (color in BGR format, thickness in pixels)
cv2.line(image, (50, 50), (450, 50), (0, 0, 255), 2)

# Draw a circle (center coordinates, radius, color, thickness)
cv2.circle(image, (250, 250), 100, (0, 255, 0), 2)

# Draw a rectangle (top-left and bottom-right corners, color, thickness)
x, y, w, h = 100, 100, 300, 300
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Draw a polygon (list of vertices, color, thickness)
points = np.array([[200, 200], [300, 200], [350, 300], [250, 350], [150, 300]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(image, [points], isClosed=True, color=(0, 255, 255), thickness=2)


# Display the image
cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()