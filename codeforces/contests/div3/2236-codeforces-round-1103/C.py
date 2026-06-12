from collections import deque
t=int(input())
for _ in range(t):
    a,b,x=list(map(int,input().split()))
    if a == b:
        print(0)
        continue
    if abs(a - b) == 1:
        print(1)
        continue
        
    dista = []
    cur_dist = 0
    cur = a
    while True:
        dista.append((cur, cur_dist))
        if cur == 0:
            break
        cur //= x
        cur_dist += 1
        
    distb = []
    cur_dist = 0
    cur = b
    while True:
        distb.append((cur, cur_dist))
        if cur == 0:
            break
        cur //= x
        cur_dist += 1
        
    res = float('inf')
    for va, sa in dista:
        for vb, sb in distb:
            if va <= vb:
                res = min(res, sa + sb + (vb - va))
            else:
                res = min(res, sa + sb + (va - vb))
                
    print(res)
