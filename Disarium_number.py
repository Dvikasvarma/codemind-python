import math

a = int(input())
b = a
co = 0
s = 0

temp = a
while temp != 0:
    temp = temp // 10
    co += 1

temp = a
while temp != 0:
    r = temp % 10
    s += math.pow(r, co)
    co -= 1
    temp = temp // 10
    
if b == int(s):
    print("True")
else:
    print("False")
