import dlib
import cv2

# Load face detector
detector = dlib.get_frontal_face_detector()

# Input video
cap = cv2.VideoCapture("vid.mp4")

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    # Draw bounding boxes
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Write frame to output video
    out.write(frame)

# Release everything
cap.release()
out.release()

print("Output video saved as output.mp4")
