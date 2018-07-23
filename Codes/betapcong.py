import stdio
a = stdio.readString()
b = stdio.readString()

if len(a) < len(b):
	temp = a
	a = b
	b = temp
for i in range(0,abs(len(a)-len(b))):
	b = '0' + b
reb = 0
reb_no = 0
for i in range(len(a)-1,-1,-1):
	res = int(a[i])+ int(b[i]) + reb
	if res >= 10:
		reb = 1
		reb_no += 1
	else:
		reb = 0
print('The number of remember of a + b is: ' + str(reb_no)) 
