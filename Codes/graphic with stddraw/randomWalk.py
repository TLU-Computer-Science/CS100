import stddraw
import sys
import math
import random

n = int(sys.argv[1])
stddraw.setXscale(-n, +n)
stddraw.setYscale(-n, +n)
stddraw.clear(stddraw.GRAY)

x = 0
y = 0

steps = 0
while (abs(x) < n and abs(y) < n):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledSquare(x, y, 0.45)
    r = random.randrange(0,10)/10
    if r < 0.25:
        x -= 1
    elif r < 0.50:
        x += 1
    elif r < 0.75:
        y -= 1
    elif r < 1.00:
        y += 1
    steps += 1
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.filledSquare(x, y, 0.45)
    stddraw.show(40)