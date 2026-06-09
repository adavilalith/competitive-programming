from math import *
from collections import defaultdict
t=int(input())
for _ in range(t):
    # print("############")
    n=int(input())
    res=[]
    for i in range(1,n+1):
        res.append(i)
        res.append(i)
    for i in range(1,n+1):
        res.append(i)
    for i in range(1,n+1):
        res.append(i)
    res.pop()
    res=[n]+res
    # d=defaultdict(list)
    # for i,x in enumerate(res):
    #     d[x].append(i)
 
    # for x in d:
    #     s=set()
    #     s.add(d[x][1]-d[x][0])
    #     s.add(d[x][2]-d[x][1])
    #     s.add(d[x][3]-d[x][2])
    #     if len(s)!=3:
    #         print(x,d[x],s)
    #         print(d[x][1]-d[x][0])
    #         print(d[x][2]-d[x][1])
    #         print(d[x][3]-d[x][2])
    #         print("INVALID")
    for x in res:
        print(x,end=" ")
    print()
 
# 1 1 2 2 3 3 1 2 3 1 2 3 