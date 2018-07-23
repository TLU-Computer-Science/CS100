# python oscilloscope.py 1 1 2 3 20 45
# python oscilloscope.py 1 1 5 3 30 45
import stddraw
import sys
import math

stddraw.setXscale(-1, +1)
stddraw.setYscale(-1, +1)
stddraw.setPenRadius(0.01)

A    = float(sys.argv[1])    # amplitudes
B    = float(sys.argv[2])
wX   = float(sys.argv[3])    # angular frequencies
wY   = float(sys.argv[4])
phiX = float(sys.argv[5])    # phase factors
phiY = float(sys.argv[6])

# Convert from degrees to radians.
phiY = math.radians(phiX)
phiY = math.radians(phiY)

t = 0.0
while True:
    x = A * math.sin(wX * t + phiX)
    y = B * math.sin(wY * t + phiY)
    stddraw.point(x, y)
    stddraw.show(10.0)
    t += 0.01
    #t += 0.0001
