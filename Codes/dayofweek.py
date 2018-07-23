import stdio
import sys

d = int(sys.argv[1])
m = int(sys.argv[2])
y = int(sys.argv[3])

y0 = y - ( 14-m)/12
x = y0 + y0/4 -y0/100 +y0/400
m0 = m +12*((14-m)/12)-2
d0 = int((d+x+(31*m0)/12))%7
stdio.writeln(d0)