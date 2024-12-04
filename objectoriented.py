#This will be an object oriented vesion 
# of the virtual3d game

import cv2 
import numpy as np

class Tunnel:
  def __init__(self):
    """Maps a 3d point to 2d screen. Assumes user is at (0,0,0).
    EXAMPLE: (25,12.5,75) --> (row,col)
    """
    # CONSTANTS
    self.SCREEN_WIDTH = 20
    self.SCREEN_HEIGHT = 10
    self.SCREEN_PIXEL_WIDTH = 1920
    self.SCREEN_PIXEL_HEIGHT = 1080
    self.DIST_USER_TO_SCREEN = 25 # distance from the screen
    self.DIST_SCREEN_TO_TUNNEL = 50
    self.TUNNEL_WIDTH = 50
    self.TUNNEL_HEIGHT = 25

    # TUNNEL - four rectangles:
    #RECT0 = [[],[]]                       # [[top left ],[bottom right]]
    self.RECT0 = ((-25,-12.5,75),(25,12.5,75))   # [[x,y,z],[x,y,z]]
    self.RECT1 = ((-25,-12.5,125),(25,12.5,125))
    self.RECT2 = ((-25,-12.5,175),(25,12.5,175))
    self.RECT3 = ((-25,-12.5,225),(25,12.5,225))

    self.LINE0 = ((-25,-12.5,75),(-25,-12.5,225))
    self.LINE1 = ((25,12.5,75),(25,12.5,225))
    self.LINE2 = ((-25,12.5,75),(-25,12.5,225))
    self.LINE3 = ((25,-12.5,75),(25,-12.5,225))

    # the frame variable will hold our display pixels self.frame is an ndarray
    self.frame = np.zeros([self.SCREEN_PIXEL_HEIGHT,
                          self.SCREEN_PIXEL_WIDTH,
                          3])                         # three colors, RGB

  def threeD2twoD(s, xyz):
    """Maps a 3d point to 2d screen. Assumes user is at (0,0,0).
    EXAMPLE: (25,12.5,75) --> (row,col)
    """
    obj_x, obj_y, obj_z = xyz
    screen_z = s.DIST_USER_TO_SCREEN
    #  screen_x    obj_x
    #  -------- = ----------
    #  screen_z    obj_z

    screen_x = obj_x * screen_z / obj_z
    screen_x_px = (1920/20)* screen_x
    row = 1920/2 + screen_x_px

    #  screen_y    obj_y
    #  -------- = ----------
    #  screen_z    obj_z

    screen_y = obj_y * screen_z / obj_z
    screen_y_px = (1080/10)* screen_y
    col = 1080/2 + screen_y_px

    return (int(row),int(col))

  def draw_rectangle(self, rect_coords): #draw rectangles on the screen
    """Convert rectcoords from 3d to 2d, then call opencv rectangle"""
    tl_row, tl_col = self.threeD2twoD(rect_coords[0])
    br = self.threeD2twoD(rect_coords[1])

    cv2.rectangle(self.frame,(tl_row,tl_col),     # top left
              br,                  # bottom right
              (0,0,255),           # color
              2)                   # line thickness

  #-----------------------------------------------
  # TODO 1
  # INSERT DRAWLINE METHOD BELOW
  def draw_line(self, line_coords):
    """The draw_line member function will draw diagonal tunnel elements
    More specically this function should appropriately:
    self.LINE0 = ((-25,-12.5,75),(-25,-12.5,225))
    where the first tuple represents the x,y,z of the line starting point in 3d, and the second tuple represents the line end point in 3d.

    The draw_line member function should appropriately:

    convert the start and end points from 3d to 2d
    call OpenCV's cv.line function, to draw a red line onto the self.frame attribute ndarray so that the line shows up in the final drawing of the tunnel (see the image below at the end to see what your answer should look like).
    """

    print('This is draw_line')
    #convert the start and end points from 3d to 2d
    start_point = line_coords[0]
    end_point = line_coords[1]
    start_point2d = row, col = my_game.threeD2twoD(start_point)
    end_point2d = my_game.threeD2twoD(end_point)

    #call cv.line to draw a red line onto the self.frame
    cv2.line(self.frame, start_point2d, end_point2d, (0,0,255))
    
    # INSERT DRAWLINE METHOD ABOVE
    # END TODO 1
    #-----------------------------------------------


  def display_tunnel(self):
    """ Draw the four rectangles for tunnel and the circle """

    # first draw a circle in the center of the screen as a "vanishing point"
    cv2.circle(self.frame,
               (960,540),      # center point
               5,              # radius
               (255,255,255),  # color
               -1)             # line thickness, -1 for fill
    #Code below was initialized in the init function.
    self.draw_rectangle(self.RECT0)
    self.draw_rectangle(self.RECT1)
    self.draw_rectangle(self.RECT2)
    self.draw_rectangle(self.RECT3)

    #-----------------------------------------------
    # TODO 2:
    # Call the draw_line method below for each of: LINE0, LINE1, LINE2, LINE3

    #self.draw_line(((-25,12.5,75),(-25,-12.5,225)))
    self.draw_line(self.LINE0)
    self.draw_line(self.LINE1)
    self.draw_line(self.LINE2)
    self.draw_line(self.LINE3)

    # Call the draw_line method above
    # END TODO 2
    #-----------------------------------------------

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
                bx, by, bw, bh = x,y,w,h

        cv2.rectangle(frame, (bx, by), (bx+bw, by+bh), (0, 255, 255), 3)

        return((bx+bw//2), (by+bh//2))

class Stage: #often called in video game programming

 def __init__(self):
   self.disp_h = 0
   self.disp_w = 0
   self.cam_h = 720
   self.cam_w = 1280
   self.save_x = 960 #x position being saved between frame

 def draw_target_xy(self, img, pos, size): #draws target in appropiate position given users position

   cv2.circle(img, pos, size, (0, 0, 255), -1) #color is white and -1 is a full circle
            
   cv2.circle(img, pos, int(size*.8), (255, 255, 255), -1)

   cv2.circle(img, pos, int(size *.6), (0, 0, 255), -1)
   
   cv2.circle(img, pos, int(size* .4), (255, 255, 255), -1)

   cv2.circle(img, pos, int(size*.2),(0, 0, 255), -1) 
           

   
 def draw_targetz(self, pos, facexy): #draws target in appropiate position given users position
   tx, ty, tz = pos 
   cv2.circle(img, (ball0x , ball0y), 
             50, (255, 0, 0), -1)
   cv2.line(img,(960+ int((600-960)*.3**2), 540), (ball0x, ball0y), (255,0,0),3)
 

 def update(self, facexy):#draws tunnel and targets based on user position
    x,y= facexy
    e = .9 # smoothing constant
    x = e * x + (1-e)*self.save_x
    img = np.zeros([1080,1920,3])
    decay = .3
    sx = sy = 0
    dx = int((x - self.cam_w/2)*2)
    for i in range(1,7):
      sx = sx + int((960-sx)*decay)
      sy = sy + int((540-sy)*decay)
      dx = int(dx * decay)
      #print(sx, sy)
      cv2.rectangle(img, (sx+dx,sy),(1920-sx+dx, 1080-sy), (255,255,255), 1)

      ball0x = 600+ int((x - self.cam_w/2)*2*.6)
      ball0y = 540

      cv2.line(img,(960+ int((600-960)*.3**2), 540),(ball0x, ball0y), (255,0,0),3)
      self.draw_target_xy(img, (ball0x, ball0y), 35)

      ball1x = 1000+ int((x - self.cam_w/2)*2*.2)
      ball1y = 440

      cv2.line(img,  
               (960+ int((1200-960)*.3**2), 540 - int((540-340)*.3**2)),
               (ball1x,ball1y),
               (255,0,0),3)

      self.draw_target_xy(img, (ball1x, ball1y), 25)

      ball2x = 1100+ int((x- self.cam_w/2)*2*.9)
      ball2y = 650
      
      cv2.line(img, 
               (960+ int((1100-960)*.3**2), 540 - int((540-650)*.3**2)),
               (ball2x, ball2y), 
               (255,0,0),3)


      self.draw_target_xy(img, (ball2x, ball2y), 50)

      cv2.imshow('Ronnals Game', img)



#---------------------------------------------------------------------------
#main
print('starting OO virtual3d.')# baby step to make sure machine is working
ff = FaceFinder()#creating facefinder instance

stage = Stage()#responsible for rendering

img = np.zeros([1080,1920,3])#ndarray that initializes with zeros

cv2.imshow('Game', img) #initialize game window

cap = cv2.VideoCapture(cv2.CAP_ANY)# initialize web cam

if not cap.isOpened():
  print("Couldn't open camera. Make sure you have a web camera that is not being used by another app.")
  exit()

moved = False
while True:
  # Reads the frame
  ret, frame = cap.read()

  if not ret:
    print("Error reading the frame. Exiting...")

  facexy = ff.find_face(frame)
  frame_small = cv2.resize(frame, (frame.shape[1]//4, frame.shape[0]//4), interpolation= cv2.INTER_LINEAR)
  cv2.imshow('q to quit', frame_small) #debugs, creates seperate ha;f-sized frame

  if not moved:
   cv2.moveWindow('q to quit',1080,0) #Forces frame to go to top left corner(1080,0)

  if facexy is not None: #if no face is seen, do not update the game 
   img = stage.update(facexy)

  # Stop if q key is pressed
  if cv2.waitKey(30) == ord('q'):
    break


# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

print('virtual3d complete')
#while True: 
#  retval,frame = cap.read()
#  if retval == False:
#    print("camera error!")

#  ff.find_face(frame)
#  cv2.imshow('q to quit', frame)

#  if cv2.waitKey(30) == ord('q'):
#    break

#pause = input('press enter to end')


#destroy cam
#cap.release()

#cv2.destroyAllWindows()

