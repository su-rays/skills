import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture("/home/su-rays/projects/skills/libraries/opencv/data/people_walking.mp4")

# Read the first frame
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Create a VideoWriter object to save the stabilized video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('stabilized_video.avi', fourcc, 20.0, (640, 480))

# Initialize transformation matrix
transform = np.eye(2, 3, dtype=np.float32)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Estimate affine transformation
    dx = np.mean(flow[..., 0])
    dy = np.mean(flow[..., 1])
    transform[0, 2] += dx
    transform[1, 2] += dy

    # Apply affine transformation to stabilize the frame
    stabilized_frame = cv2.warpAffine(frame, transform, (frame.shape[1], frame.shape[0]))

    # Write the stabilized frame to the output file
    out.write(stabilized_frame)

    # Display the stabilized frame
    cv2.imshow('Stabilized Video', stabilized_frame)

    # Update the previous frame
    prev_gray = gray.copy()

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()