import stddraw
import stdaudio
import math
import picture
rx = 0.480; ry = 0.860     # position
vx = 0.015; vy = 0.023     # velocity
radius = 0.05              # radius
# set the scale of the coordinate system
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
while True :
    # bounce off wall according to law of elastic collision
    if abs(rx + vx) + radius > 1.0:
        vx = -vx
        stdaudio.playFile("pipebang")
    if abs(ry + vy) + radius > 1.0:
        vy = -vy
        stdaudio.playFile("pipebang")
    # update position
    rx = rx + vx
    ry = ry + vy 
    # set the background to light gray
    stddraw.clear(stddraw.LIGHT_GRAY)
    # draw ball on the screen
    pic = picture.Picture("TennisBall.png")
    stddraw.picture(pic,rx, ry)
    # display and pause for 20ms
    stddraw.show(20)
