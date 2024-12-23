import cv2
import numpy as np
import matplotlib.pyplot as plt


class Game:
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



  def start_loop(self):
    """Runs a while loop """
    while True:
      # get face position


      # zero frame
      self.frame = np.zeros([self.SCREEN_PIXEL_HEIGHT,
                            self.SCREEN_PIXEL_WIDTH,
                            3])                         # three colors

      # draw tunnel from user's perspective
      self.display_tunnel()

      # temp code start-------------
      cv2.imshow('Ronnals game', self.frame)
      #break
      # temp code stop--------------

      #cv2.imshow(self.frame)
      if cv2.waitKey(1) == ord('q'):
        break

    print('game over')


my_game = Game()#creating a game instance and putting it inside my_game.start.loop()
my_game.start_loop()
cv2.destroyAllWindows()