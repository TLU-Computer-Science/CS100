import stdio
n = stdio.readString()
    
n = list(n)   
i = len(n)-1 
check = True
while i >= 0:
    if n[i] == '0':
        n[i] = '1'
        check = False
        break
    else:
        n[i] = '0'
    i = i-1
binar = ''.join(n)
if check:
    binar = '1'+binar
stdio.writeln(binar)