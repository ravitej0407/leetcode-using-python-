import sys
num = input('enter a number : ')
for i in range(len(num)-1,-1,-1):
 if int(num[i])%2 == 1:
  print(num[:i+1])
  sys.exit(0)


