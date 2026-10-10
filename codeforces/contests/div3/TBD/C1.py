import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
def invr():
    return(map(int,input().split()))

t=inp()
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    if (a[::2].count("1") == b[::2].count("1")) and (
        a[1::2].count("1") == b[1::2].count("1")
    ):
        print("YES")
    else:
        print("NO")