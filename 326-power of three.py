a = input('Enter a number : ')
a = int(a)
def power(n :int)->bool:
    if(n<=0):
        return False
    if(n == 1):
        return True
    if(n%3 == 0):
        return power(n/3)
    return False
print(power(a))

