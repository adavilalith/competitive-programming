t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    st=[]
    pairs=[]
    i=0
    while i<n:
        if s[i]=='(':
            st.append(i)
        else:
            if len(st)>0:
                left=st.pop()
                right=i
                pairs.append((left,right))
        i+=1
    pvt=n+1
    while st:
        pvt=st.pop()
    rm_chars=[]
    for l,r in pairs:
        if l<pvt:
            if k>0:
                rm_chars.append(l)
                k-=1
        elif r>pvt:
            if k>0:
                rm_chars.append(r)
                k-=1
    res=["0"]*n
    for i in rm_chars:
        res[i]="1"
    res=''.join(res)
    print(res)