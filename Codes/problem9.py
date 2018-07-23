import math
a = 1
b = 2
c = 0
a_max = 332
b_max = 499
while a + b + c != 1000:
    if a + 1 < b and a <= a_max:
        a += 1
    else:
        b += 1
        a = 1
    c = math.sqrt(a ** 2 + b ** 2)
print(int(a * b * c))
