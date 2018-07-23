import stdio
import stddraw
y = 1
check = False
for i in range(1000):
	stddraw.clear()
	stddraw.circle(0.5,y,0.1)
	stddraw.show(120)
	if y <= 0:
		check = False
	if y >= 1:
		check = True
	if check == True:
		y = y - 0.1
	else:
		y = y + 0.1
    
