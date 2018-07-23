import stddraw
import sys
import math

stddraw.setXscale(-1.5,1.5)
stddraw.setYscale(-1.5,1.5)
stddraw.setPenColor(stddraw.PINK)

xs = [ -1,  0, 1, 0 ]
ys = [  0, -1, 0, 1 ]
stddraw.filledPolygon(xs, ys)

stddraw.filledCircle(+0.5, 0.5, 1 / math.sqrt(2))
stddraw.filledCircle(-0.5, 0.5, 1 / math.sqrt(2))

stddraw.show()
