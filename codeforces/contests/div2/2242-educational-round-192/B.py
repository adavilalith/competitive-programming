import sys
input = sys.stdin.readline
from collections import Counter

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t=inp()
for _ in range(t):
    n=inp()
    a=inlt()
    memo={}
    def solve(i=0,c=0):
        res=False
        d1={}
        d2={}
        if c==2 and i<n:
            memo[i,c]=True
            return True
        if (i,c) in memo:
            return memo[i,c]
        if c==0:
            while i<n and not res:
                d1[a[i]]=1+d1.get(a[i],0)
                if d1.get(1,0)>=1 and d1.get(1,0)>=(d1.get(2,0)+d1.get(3,0)) :
                    res=solve(i+1,c+1) or res
                i+=1
            memo[i,c]=res
            return memo[i,c]
        if c==1:
            while i<n and not res:
                d2[a[i]]=1+d2.get(a[i],0)
                if (d2.get(2,0)>=1 or d2.get(1,0)>=1) and (d2.get(1,0)+d2.get(2,0))>=d2.get(3,0) :
                    res=res or solve(i+1,c+1)
                i+=1
            memo[i,c]=res
            return memo[i,c]
    if solve(0,0):
        print("YES")
    else:
        print("NO")