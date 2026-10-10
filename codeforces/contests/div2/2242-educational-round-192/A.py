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
    k=inp()
    ck=inlt()
    res=True
    c=Counter(ck)
    for k in c:
        if k==1:
            continue
        elif k==2:
            if c[k]>=2:
                res=False
                print("YES")
                break
        elif c[k]>=1:
            res=False
            print("YES")
            break
    if res:
        print("NO")