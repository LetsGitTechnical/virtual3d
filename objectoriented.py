#This will be an object oriented vesion 
# of the virtual3d game

import cv2 

class FaceFinder:
    """Use haar cascade filter to find the largest face in a frame"""

    def __init__(self):
        print('Face Finder initialize')
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def find_face(self, frame):
        """Returns face center(x,y), draws rectangle on the frame"""
        # convert to grayscale
        gray = cv2.cvtColor(frame,cv2.BGRZGRAY) 
        faces = self.face_cascade.detectMulti(gray,MinNeighbors=q)

            #drawrect 
        if faces is None: 
            return None 
        bx=by=bw=bh = 0

        for (x, y, w, h) in faces:
            if w > bw: 
                bx,by, bw, bh = x,y,w,h

        cv2.rectangle(img, (bx, by), (bx+bw, by+bh), (0, 255, 255), 3)

        return((bx+bw//2), (by+bh//2))

#----------------------------------------
#main
print('starting OO virtual3d.')# baby step to make sure machine is working

ff = FaceFinder()
print('virtual3d complete')
