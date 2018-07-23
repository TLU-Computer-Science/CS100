import stdio
N = stdio.readInt()

k = N
while k >= 6:
	i = 2 
	tong = 1
	while i <= int(k/2):
		if k % i == 0:
			tong += i
		i += 1

	if tong == k:
		print(k)
		break
	k -= 1
