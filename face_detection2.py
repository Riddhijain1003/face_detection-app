import cv2
import dlib


detector = dlib.get_frontal_face_detector()


cap = cv2.VideoCapture("video.mp4")   

if not cap.isOpened():
    print("Error opening video file")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break   
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    faces = detector(gray)

    
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    
    cv2.imshow("Video Face Detection", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()