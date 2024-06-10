import cv2
from PIL import Image

clasificador = 'haarcascade_frontalface_default.xml'

def anonymisation(output_file, image_to_anonymise):
    image = cv2.imread(image_to_anonymise)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(clasificador)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))


    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x+w]
        blurred_face = cv2.resize(cv2.resize(face, (w//10, h//10)), (w, h))
        image[y:y+h, x:x+w] = blurred_face

    cv2.imwrite(output_file, image)

    return Image.open(output_file)