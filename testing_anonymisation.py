import cv2

clasificador = 'haarcascade_frontalface_default.xml'

image_path = 'messi.jpg'

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(clasificador)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))

# Dibujamos rectangulos alrededor de las caras detectadas
for (x,y,w,h) in faces:
    #cv2.rectangle(image,(x,y), (x+w, y+h), (0,255,0),2)
    face = image[y:y+h, x:x+w]
    blurred_face = cv2.resize(cv2.resize(face, (w//10, h//10)), (w,h))
    image[y:y+h, x:x+w] = blurred_face


cv2.imshow('Faces Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()