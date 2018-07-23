import stddraw
import sys

n = int(sys.argv[1])
add = float(sys.argv[2])

x = 0.0
i = 0
while i < n:
	if i % 2 == 0:
		stddraw.line(x,0.3,x+add,0.2)
	else:
		stddraw.line(x,0.2,x+add,0.3)
	stddraw.show(60)
	x = x + add
	i = i + 1
stddraw.show()