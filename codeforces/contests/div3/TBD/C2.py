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

def solveParity(a, b, start):
    pa = []
    pb = []
    idx = 0
    n = len(a)
    for i in range(start, n, 2):
        if a[i] == '1':
            pa.append(idx)
        if b[i] == '1':
            pb.append(idx)
        idx += 1
    cost = 0
    for x, y in zip(pa, pb):
        cost += abs(x - y)
    return cost

t=inp()
for _ in range(t):
    n = inp()
    a = insr()
    b = insr()

    e1a = e1b = o1a = o1b = 0
    for i in range(n):
        if i % 2 == 0:
            e1a += (a[i] == '1')
            e1b += (b[i] == '1')
        else:
            o1a += (a[i] == '1')
            o1b += (b[i] == '1')

    if e1a != e1b or o1a != o1b:
        print(-1)
        continue

    ans = solveParity(a, b, 0) + solveParity(a, b, 1)
    print(ans)