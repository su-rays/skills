import cv2
import numpy as np

# Create a black image
img = np.zeros((300, 500, 3), dtype=np.uint8)

# Create a named window
cv2.namedWindow("Resizable Window", cv2.WINDOW_NORMAL)

# Resize the window
cv2.resizeWindow("Resizable Window", 800, 600)

# Move the window to a specific position
cv2.moveWindow("Resizable Window", 100, 100)

# Display the image in the window
cv2.imshow("Resizable Window", img)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()