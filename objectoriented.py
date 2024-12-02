#This will be an object oriented vesion 
# of the virtual3d game

import cv2 

class Tunnel:
  pass


class FaceFinder:
    """Use haar cascade filter to find the largest face in a frame"""

    def __init__(self):
      print('Face Finder initialize')
      self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def find_face(self, frame):
        """Returns face center(x,y), draws rectangle on the frame"""
        # convert to grayscale
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        faces = self.face_cascade.detectMultiScale(gray,minNeighbors=9)

            #drawrect 
        if faces is None: 
            return None 

        bx=by=bw=bh = 0

        for (x, y, w, h) in faces:
            if w > bw : 
                bx,by, bw, bh = x,y,w,h

        cv2.rectangle(frame, (bx, by), (bx+bw, by+bh), (0, 255, 255), 3)

        return((bx+bw//2), (by+bh//2))

#----------------------------------------
#main
print('starting OO virtual3d.')# baby step to make sure machine is working
ff = FaceFinder()

cap = cv2.VideoCapture(cv2.CAP_ANY)

if not cap.isOpened():
  print("Couldn't open cam")
  exit()





while True: 
  retval,frame = cap.read()
  if retval == False:
    print("camera error!")

  ff.find_face(frame)
  cv2.imshow('q to quit', frame)

  if cv2.waitKey(30) == ord('q'):
    break

#pause = input('press enter to end')


#destroy cam
cap.release()

Cv2.destroyAllWindows()
print('virtual3d complete')
