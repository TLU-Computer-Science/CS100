import stdio
N = stdio.readInt()
M = stdio.readInt()
i = N - M
while i <= M:
	tick = str(i)
	check = False
	for j in range(1,len(tick)):
		if tick[j]!=tick[0]:
			check = True
			break
	if not check:
		print(tick)
	i += 1
		

