import sys
import stdio

N = int(sys.argv[1])

a = []

for i in range(0,N):
	a.append(int(sys.argv[2+i]))

print(a)

for i in range(0,N):
	for j in range(i+1,N):
		if a[i] > a[j]:
			t = a[i]
			a[i] = a[j]
			a[j] = t
print(a)