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

import heapq

t=inp()
for _ in range(t):
    n,m=inlt()
    a=inlt()
    
    if m == 1:
        print(max(a))
        continue
        
    max_heap = []   
    sum_smallest = 0
    ans = -float('inf')
    
    for i in range(n):
        x = a[i]
        
        if len(max_heap) == m - 1:
            current_score = m * x - sum_smallest
            if current_score > ans:
                ans = current_score
                
        heapq.heappush(max_heap, -x)
        sum_smallest += x
        
        if len(max_heap) > m - 1:
            largest_in_heap = -heapq.heappop(max_heap)
            sum_smallest -= largest_in_heap
            
    print(ans)
