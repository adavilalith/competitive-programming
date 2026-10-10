import sys
from collections import deque
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

good_set = set()

for d1 in range(10):
    for d2 in range(d1 + 1, 10):
        q = deque()
        if d1 > 0: 
            q.append(d1)
        if d2 > 0: 
            q.append(d2)
        
        while q:
            val = q.popleft()
            good_set.add(val)
            
            if val < 10**12:
                q.append(val * 10 + d1)
                q.append(val * 10 + d2)

good_list = sorted([y for y in good_set if y >= 2])

def is_good(n):
    return len(set(str(n))) <= 2
    
t = inp()
for _ in range(t):
    x = inp()  
    
    for y in good_list:
        if x * y in good_set:
            print(y)
            break   