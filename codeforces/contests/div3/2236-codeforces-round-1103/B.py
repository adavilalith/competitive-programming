t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    arr=[0]*n
    for i in range(n):
        if s[i]=="1":
            arr[i%k]+=1
    cond=True
    for x in arr:
        if x%2!=0:
            cond=False
            break
    if cond:
        print("YES")       
    else:
        print("NO")

'''
STANDARD INPUTS
n=int(input())
n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
s=input()
'''
