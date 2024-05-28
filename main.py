import cv2
import numpy as np
import os

# Define the ASCII characters based on brightness levels
ASCII_CHARS = " .:-=+*#%@"


def clear_console():
    # Check the operating system and execute the appropriate command
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Unix/Linux/MacOS
        os.system("clear")


def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (
            int(w * r),
            height,
        )  # Multiply width by 2 for aspect ratio adjustment
    else:
        r = width / float(w)
        dim = (width, int(h * r))  # Multiply width by 2 for aspect ratio adjustment
    return cv2.resize(image, dim, interpolation=inter)


def pixel_to_ascii(image):
    # Convert each pixel to corresponding ASCII character
    ascii_str = ""
    num_chars = len(ASCII_CHARS)
    for row in image:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel * num_chars // 256]  # Map pixel to ASCII
        ascii_str += "\n"
    return ascii_str


def adjust_contrast(image, alpha=1, beta=10):
    # Adjust the contrast of the image
    new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return new_image


# Define a video capture object
vid = cv2.VideoCapture(2)

# Check if the camera opened successfully
if not vid.isOpened():
    print("Error: Could not open video device")
    exit()

# Set the desired maximum width and height
max_width = 160  # Adjust width for ASCII
max_height = 80  # Adjust height for ASCII

while True:
    # Capture the video frame by frame
    ret, frame = vid.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Resize the current frame while keeping the aspect ratio
    frame_resized = resize_with_aspect_ratio(frame, width=max_width, height=max_height)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Apply a contrast filter to the grayscale image
    contrast_frame = adjust_contrast(gray_frame)

    frame_2x_width = cv2.resize(
        contrast_frame, (max_width * 2, max_height), interpolation=cv2.INTER_AREA
    )

    # Convert pixels to ASCII characters
    ascii_str = pixel_to_ascii(frame_2x_width)

    clear_console()
    cv2.imshow("ASCII Video", contrast_frame)
    # cv2.imshow("Input Video", frame)
    print(ascii_str)

    # 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
