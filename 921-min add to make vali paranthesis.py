a = input('Enter the string : ')
d = 0
for i in a:
    if(i == '('):
        d += 1
    elif (i == ')'):
        d -= 1
print(abs(d))

