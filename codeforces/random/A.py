import sys
input = sys.stdin.readline

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
    cond=True
    bad=[]
    for i in range(n):
        if a[i]!=i+1:
            bad.append(i)
    l,r=0,len(bad)-1
    while l<=r:
        if a[bad[r]]==bad[l]+1 and a[bad[l]]==bad[r]+1:
            l+=1
            r-=1
        else:
            cond=False
            break
    if cond:
        print("YES")
    else:
        print("NO")