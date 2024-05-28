import cv2
import numpy as np

# Define a video capture object
vid = cv2.VideoCapture(2)

ret, frame = vid.read()

while True:
    latest_frame = frame

    # Capture the video frame by frame
    ret, frame = vid.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the resulting frame difference
    frame_diff = cv2.absdiff(frame, latest_frame)

    # Add the current frame with 0.5 opacity
    blended_frame = cv2.addWeighted(frame, 0.1, frame_diff, 1, 0)

    # Display the frame
    cv2.imshow("frame", blended_frame)

    # 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
