import cv2

# Open the video file
cap = cv2.VideoCapture("/home/su-rays/projects/skills/libraries/opencv/data/people_walking.mp4")

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame (e.g., convert to grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the processed frame to the output file
    out.write(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR))

    # Display the frame
    cv2.imshow('Processed Video', gray_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()