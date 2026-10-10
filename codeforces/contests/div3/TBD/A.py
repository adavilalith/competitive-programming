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
    a,b,c=inlt()
    turn=0
    while True:
        if a==b or b==c or a==c:
            break
        if a>b and a>c:
            a-=1
            if b>c:
                c+=1
            else:
                b+=1
        elif b>c and b>a:
            b-=1
            if a>c:
                c+=1
            else:
                a+=1
        else:
            c-=1
            if b>a:
                a+=1
            else:
                b+=1
        turn+=1
    print(turn)