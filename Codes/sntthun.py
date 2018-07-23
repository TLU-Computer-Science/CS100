import stdio
import math
N = stdio.readInt()
L = 3
k = 2 # so nguyen to thu
while True:
	Flag = True
	for i in range(2,int(math.sqrt(L)) + 1):
		if L % i == 0:
			Flag = False
			break
	if Flag:
		if k == N:
			print(L)
			break
		k += 1
	L += 2