import cv2
import dlib 

image = cv2.imread("faces.jpeg")

if image is None:
    print("Image not found!")
    exit()

print(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("#########")
print(gray)

detector = dlib.get_frontal_face_detector()
faces = detector(gray)

print("#########")
print(faces)

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    print("Face found at:", x1, y1)

    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imwrite("output.jpg", image)


cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()