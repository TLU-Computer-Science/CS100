import stdio
import sys
import math

n = int(sys.argv[1])

if n < 2:
	stdio.writeln("Ko phai la so nguyen to")
else:
	i = 2
	Flag = True
	while i <= int(math.sqrt(n)):
		if n % i == 0:
			Flag = False
		i += 1

	if Flag == True:
	 	stdio.writeln("La so nguyen to")
	else:
		stdio.writeln("Ko la so nguyen to")