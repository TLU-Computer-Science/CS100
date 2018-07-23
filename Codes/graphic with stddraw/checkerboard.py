import stdio
import stddraw
import sys
import random

stdio.write("Ban muon di truoc? [y/n]: ")
re = stdio.readString()
section = False
if re == "y":
	section = True

n = int(sys.argv[1])
m = int(sys.argv[2])
if n > m:
	stddraw.setXscale(0, n)
	stddraw.setYscale(0, n)
else:
	stddraw.setXscale(0, m)
	stddraw.setYscale(0, m)
No_ = m*n
while True:
	no_run = 0
	stddraw.clear()
	if No_ > 0:
		for i in range(n):
			for j in range(m):
				if no_run < No_:
					stddraw.setPenColor(stddraw.RED)
					stddraw.filledCircle(i + .5, j + .5, .5)
					no_run += 1
		stddraw.show(20)
		if section:
			stdio.write("Luot choi cua ban[1-3]: ")
			k = stdio.readInt()
			No_ -= k
			section = False
		else:
			
			if No_%4 == 1:
				k = random.randrange(1,4)
			elif No_ % 4 == 0:
				k = 3
			else:
				k = No_ % 4 -1
			
			stdio.writeln("Toi chon " + str(k))
			No_ -= k
			stddraw.show(120)
			section = True
	else:	
		if section:
			stdio.writeln("Chuc mung, Ban da thang!")
			break
		else:
			stdio.writeln("Toi Thang!")
			break
stddraw.show()
	
