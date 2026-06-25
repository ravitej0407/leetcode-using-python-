a = input('enter the string : ')
d = 0
m = 0
for i in a:
    if(i == '('):
        d += 1
        if(m < d):
            m = d
    elif(i == ')'):
        d -= 1
print(m)

