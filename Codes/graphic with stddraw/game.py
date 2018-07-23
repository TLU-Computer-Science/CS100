import stdio
import stddraw
import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
if n > m:
	stddraw.setXscale(0, n)
	stddraw.setYscale(0, n)
else:
	stddraw.setXscale(0, m)
	stddraw.setYscale(0, m)
section = True
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
		print(section)
		if section:
			stdio.write("Luot choi cua A[1-3]: ")
			k = stdio.readInt()
			No_ -= k
			section = False
		else:
			stdio.write("Luot choi cua B[1-3]: ")
			k = stdio.readInt()
			No_ -= k
			section = True
	else:	
		if section:
			stdio.writeln("A Thang")
			break
		else:
			stdio.writeln("B Thang")
			break
stddraw.show()
	
