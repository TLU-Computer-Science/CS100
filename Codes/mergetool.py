s = input()
k = int(input())
print (len(s))
for i in range(len(s) // k):
	t = ''
	for c in s[i * k : (i + 1) * k]:
		if c in t:
			continue
		t += c
	print (t)