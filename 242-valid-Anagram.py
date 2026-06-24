a = input('enter the string1 : ')
b = input('enter the string2 : ')
if len(a) != len(b):
    print(False)
else:
     a = sorted(a)
     b = sorted(b)
     if(a == b):
        print(True)
     else:
        print(False)





