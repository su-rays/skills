import cv2
import numpy as np

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left mouse button clicked at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right mouse button clicked at ({x}, {y})")

# Trackbar callback function
def trackbar_callback(value):
    global img
    img[:] = (value, value, value)  # Set background color based on trackbar value
    cv2.imshow("Window", img)

# Create a black image
img = np.zeros((300, 500, 3), dtype=np.uint8)

# Create a window
cv2.namedWindow("Window")

# Set mouse callback
cv2.setMouseCallback("Window", mouse_callback)

# Create a trackbar
cv2.createTrackbar("Brightness", "Window", 0, 255, trackbar_callback)

while True:
    cv2.imshow("Window", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Exit on ESC key
        break

cv2.destroyAllWindows()