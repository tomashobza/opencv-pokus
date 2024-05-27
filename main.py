import cv2

# Define a video capture object
vid = cv2.VideoCapture(1)

frame = 0

while True:
    latest_frame = frame
    # Capture the video frame by frame
    ret, frame = vid.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow("frame", latest_frame - frame)

    # 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
