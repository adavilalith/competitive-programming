
from math import *
t=int(input())
for _ in range(t):
    n,x,y,z=list(map(int,input().split()))
    #no ai:
    speed=x+y
    res=ceil(n/speed)
    #with ai
    n-=x*z
    if n<=0:
        print(res)
        continue
    else:
        speed=x+10*y
        res=min(res,ceil(n/speed)+z)
    print(res)