a = input('enter the string : ')
n = 0
def expand(l: int,r: int) -> int:
     c = 0
     while(l >= 0 and r <= (len(a)-1) and a[l] == a[r]):
        c += 1
        l -= 1
        r += 1
     return c
for i in range(len(a)):
    n += expand(i,i)
    n += expand(i,i+1)
print(n)
