import cv2

# Read two images
image1 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/cat.jpg")
image2 = cv2.imread("/home/su-rays/projects/skills/libraries/opencv/data/dog.jpeg")

# Resize images
resized_cat = cv2.resize(image1, (640, 480))
resized_dog = cv2.resize(image2, (640, 480))

# Create a Stitcher instance
stitcher = cv2.Stitcher.create()

# Stitch images
status, stitched = stitcher.stitch([resized_cat, resized_dog])

# Check if stitching was successful
if status == cv2.Stitcher_OK:
    cv2.imshow('Stitched Image', stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Stitching failed. Error code:", status)