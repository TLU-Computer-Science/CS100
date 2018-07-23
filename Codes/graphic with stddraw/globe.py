# python3 globe.py 0.95
# python3 globe.py 0.8
 
import stddraw
import sys
import math

alpha = float(sys.argv[1])
stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)
stddraw.setPenColor(stddraw.BLUE)

x0 = 1.0
y0 = 0.0
t = 0.0
while t <= 20*360.0:
	theta = math.radians(t)
	r = math.cos(alpha*theta)
	x1 = r*math.cos(theta)
	y1 = r*math.sin(theta)
	stddraw.line(x0,y0,x1,y1)
	stddraw.show(0.0001)
	x0 = x1
	y0 = y1
	t += 0.1
stddraw.show()
