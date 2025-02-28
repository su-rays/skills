import cv2
import numpy as np

def enhance_color(image_path, saturation_scale=6.0, brightness_scale=4.8):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split the HSV image into H, S, and V channels
    h, s, v = cv2.split(hsv_image)

    # Enhance saturation
    s = np.clip(s * saturation_scale, 0, 255).astype(np.uint8)

    # Enhance brightness (value)
    v = np.clip(v * brightness_scale, 0, 255).astype(np.uint8)

    # Merge the enhanced channels back
    enhanced_hsv = cv2.merge([h, s, v])

    # Convert back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2BGR)

    return enhanced_image

# Example usage
input_image_path = "/home/su-rays/projects/skills/libraries/opencv/data/elephant.jpg"
output_image_path = "enhanced_image.jpg"

# Enhance the image
enhanced_image = enhance_color(input_image_path, saturation_scale=1.5, brightness_scale=1.2)

# Save the enhanced image
cv2.imwrite(output_image_path, enhanced_image)

# Display the original and enhanced images
cv2.imshow("Original Image", cv2.imread(input_image_path))
cv2.imshow("Enhanced Image", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()