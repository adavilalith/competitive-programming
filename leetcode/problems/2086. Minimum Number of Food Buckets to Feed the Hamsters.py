class Solution:
    def minimumBuckets(self, h: str) -> int:
        if len(h)==1:
            if h=='H':
                return -1
            else:
                return 0
        res=0
        n=len(h)
        h=list(h)
        res=0
        i=0
        while i<n:
            if i==0:
                if h[i]=='H' and h[i+1]=='H':
                    return -1
            elif i==n-1:
                if h[i]=='H' and h[i-1]=='H':
                    return -1
            elif h[i]=='H' and h[i-1]=='H' and h[i+1]=='H':
                return -1
            i+=1
        i=0
        while i<n:
            if i==0:
                if h[i]=='H' and h[i+1]=='.':
                    res+=1
                    h[i+1]='F'
            elif i==n-1:
                if h[i]=='H' and h[i-1]=='F':
                    pass
                if h[i]=='H' and h[i-1]=='.':
                    h[i-1]='F'
                    res+=1
            elif h[i]=='H':
                if h[i+1]=='F' or h[i-1]=='F':
                    pass
                elif h[i+1]=='.' and h[i-1]=='.':
                    h[i+1]='F'
                    res+=1
                elif h[i+1]=='.':
                    h[i+1]='F'
                    res+=1
                elif h[i-1]=='.':
                    h[i-1]='F'
                    res+=1
            i+=1
        return res
