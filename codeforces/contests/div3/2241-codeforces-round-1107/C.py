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
    s=insr()
    res=2
    if s[0]=="0":
        flag=0
        for c in s:
            if c=="0" and flag==1:
                res=1
            if c=="1":
                flag=1 
    if s[0]=="1":
        flag=0
        for c in s:
            if c=="1" and flag==1:
                res=1
            if c=="0":
                flag=1
    if s.count('0')==n or s.count('1')==n:
        res=1 
    print(res)

