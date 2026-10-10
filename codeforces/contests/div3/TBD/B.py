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
    n = inp()
    s = insr()
    runs = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            runs += 1
    ans = runs
    for i in range(1, n - 1):
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            if s[i - 1] == s[i + 1]:
                ans = min(ans, runs - 2)
            else:
                ans = min(ans, runs - 1)
    print(ans)

