a = input('enter the string : ')
s = []
ans = ''
for i in a:
    if(i != ' '):
        s.append(i)
    else:
        s.reverse()
        ans += "".join(s) + ' '
        s = []
s.reverse()
ans += ''.join(s)
print(ans)
