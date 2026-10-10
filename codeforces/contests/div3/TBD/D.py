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
    n=inp()
    b=inlt()
    d={}
    for x in b:
        d[x]=1+d.get(x,0)
    a=list(set(b))
    a.sort()
    if a[0]!=0:
        print(-1)
        continue
    res=[]
    cond=True
    if len(a)==1:
        res=[1]*n
    else:

        res.extend([a[1]//d[a[0]]]*d[a[0]])        
        if len(a)>1:
            tot=(a[1]//d[a[0]])*d[a[0]]
            target=2
            cur=1
            while target<len(a):
                if (a[target]-tot)%(d[a[cur]])==0:
                    res.extend([(a[target]-tot)//d[a[cur]]]*d[a[cur]])
                    target+=1
                    cur+=1
                else:
                    cond=False
                    break
            res.extend([res[-1]+1]*d[a[cur]])
    for i in range(len(res)-1):
        if res[i]>res[i+1]:
            cond=False
    if cond==False:
        print(-1)
    else:
        tmp=list(set(res))
        tmp.sort()
        d={}
        for i,j in zip(a,tmp):
            d[i]=j
        ans=[]
        for i in b:
            ans.append(d[i])
        for x in ans:
            print(x,end=" ")
        print()
