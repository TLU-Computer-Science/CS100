import stddraw
import sys
import numpy
import math
# number of line segments to plot
n = int(sys.argv[1])

# the function y = sin(4x) + sin(20x), sampled at n+1 points
# between x = 0 and x = pi
x = numpy.zeros(n+1)
y = numpy.zeros(n+1)
for i in range(0,n+1):
    x[i] = math.pi * i / n
    y[i] = math.sin(4*x[i]) + math.sin(20*x[i])

# rescale the coordinate system
stddraw.setXscale(0, math.pi);
stddraw.setYscale(-2.0, +2.0);

# plot the approximation to the function
for i in range(0,n):
    stddraw.line(x[i], y[i], x[i+1], y[i+1])
    stddraw.show(50)