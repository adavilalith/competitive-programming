t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=max(a)-min(a)
    print(res+1)


'''
STANDARD INPUTS
n=int(input())
n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
s=input()
'''
