a=int(input())
co=0
for i in range(1,a):
    if a%i==0:
        co=co+i;
        
if(co>a):
    print("True")
else:
    print("False")