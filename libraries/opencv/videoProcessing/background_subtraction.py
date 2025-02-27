import cv2

# Create background subtractor objects
mog2 = cv2.createBackgroundSubtractorMOG2()
knn = cv2.createBackgroundSubtractorKNN()

# Open the video file
cap = cv2.VideoCapture("/home/su-rays/projects/skills/libraries/opencv/data/people_walking.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask_mog2 = mog2.apply(frame)
    fg_mask_knn = knn.apply(frame)

    # Display the results
    cv2.imshow('MOG2 Background Subtraction', fg_mask_mog2)
    cv2.imshow('KNN Background Subtraction', fg_mask_knn)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()