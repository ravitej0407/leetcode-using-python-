a = input("Enter a number : ")
a = int(a)
if a<=2:
    print(a)
else:
    f = 1
    se = 2
    for i in range(3,a+1):
        c = f+se
        f = se
        se = c
    print(se)

