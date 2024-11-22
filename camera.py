import numpy as np
import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Convert into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    #   detectMultScale returns an 2d ndarray
    faces = face_cascade.detectMultiScale(gray)
    print('detected face(s) at:', faces)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)
      cv2.rectangle(frame, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 0), 5)


    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()